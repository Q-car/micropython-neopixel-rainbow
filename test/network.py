import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()
wlan.isconnected()
wlan.connect('myssid', 'mypassword')
wlan.config('mac')
print(wlan.ifconfig())