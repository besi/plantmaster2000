import machine
import network

import secrets

print("Starting the WIFI...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect(secrets.wifi.ssid, secrets.wifi.password)
while not wifi.isconnected():
    machine.idle()
print("WIFI connected at %s" % wifi.ifconfig()[0])
