from network import WLAN, STA_IF
from time import sleep_ms
import secrets
import machine

def try_connection(timeout = 12):

    while not wlan.isconnected() and timeout > 0:
        print('.', end='')
        sleep_ms(500)
        timeout = timeout - 1
    return wlan.isconnected();

wlan = WLAN(STA_IF)
wlan.active(True)

# Only for deep sleep ?
# print('connecting to last AP', end='')
# print(try_connection(3))
if not wlan.isconnected():
    ap_list = wlan.scan()
    ## sort APs by signal strength
    ap_list.sort(key=lambda ap: ap[3], reverse=True)
    ## filter only trusted APs
    ap_list = list(filter(lambda ap: ap[0].decode('UTF-8') in
              secrets.wifi.aps.keys(), ap_list))
    for ap in ap_list:
        essid = ap[0].decode('UTF-8')
        if not wlan.isconnected():
            print('connecting to "', essid, end='"')
            wlan.connect(essid, secrets.wifi.aps[essid])
            print(try_connection())


# Update the time
rtc = machine.RTC()
rtc.ntp_sync(server="hr.pool.ntp.org", tz="CET-1CEST")

import gc
gc.collect()

print(wlan.ifconfig()[0])



# TODO: is this better?
# if tmo > 0:
#     print("WiFi started")
#     utime.sleep_ms(500)
#
#     rtc = machine.RTC()
#     print("Synchronize time from NTP server ...")
#     rtc.ntp_sync(server="hr.pool.ntp.org")
#     tmo = 100
#     while not rtc.synced():
#         utime.sleep_ms(100)
#         tmo -= 1
#         if tmo == 0:
#             break
#
#     if tmo > 0:
#         print("Time set")
#         utime.sleep_ms(500)
#         t = rtc.now()
#         utime.strftime("%c")
#         print("")
