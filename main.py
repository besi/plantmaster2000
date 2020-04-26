import curl
import machine
import network
import utime

import secrets

RELAIS_ENABLE = 0
RELAIS_DISABLE = 1

one_wire_pin = 4
water_relais = machine.Pin(33, machine.Pin.OUT)
water_relais.value(RELAIS_DISABLE)

# Decide when to water
water_hour = 20
water_minute = 00

watering_duration = 60  # seconds
watering_sleep_interval = 60  # seconds
loop_interval = 30  # seconds

time = utime.localtime()

one_wire = machine.Onewire(one_wire_pin)
temp_sensor = machine.Onewire.ds18x20(one_wire, 0)

mqtt = None


def send_message(message):
    print(message)
    send_message_url = (
        "https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s"
        % (secrets.telegram.token, secrets.telegram.chat_id, message)
    )
    curl.get(send_message_url)


send_message(time)
send_message("Started up")

def start_watering():

    # Read the temperature
    temp = temp_sensor.convert_read()
    temp_message = "The-temperature-is-%s-°C" % temp  # TODO: Replace the spaces
    send_message(temp_message)

    if time[0] == 1970:
        return False

    send_message("Start watering...")

    water_relais.value(RELAIS_ENABLE)
    utime.sleep(watering_duration)
    water_relais.value(RELAIS_DISABLE)
    send_message("Stopped watering")

    # Sleep for a minute so the command won't be triggered twice
    utime.sleep(watering_sleep_interval)
    print("Timer elapsed")


def conncb(task):
    mqtt.subscribe(secrets.mqtt.topic)


def datacb(msg):
    start_watering()


def init_mqtt():
    global mqtt
    mqtt = network.mqtt("MQTT", secrets.mqtt.host, connected_cb=conncb, data_cb=datacb)
    mqtt.start()


init_mqtt()

while True:

    time = utime.localtime()
    if time[3] == water_hour and time[4] == water_minute:
        send_message("Watering time...")
        start_watering()
    utime.sleep(loop_interval)
