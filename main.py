import machine
import utime

one_wire_pin = 4

one_wire = machine.Onewire(one_wire_pin)
temp_sensor = machine.Onewire.ds18x20(one_wire, 0)

while True:
    temp = temp_sensor.convert_read()
    print(temp)
    utime.sleep(5)
