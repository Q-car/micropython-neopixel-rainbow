# micropython-neopixel-rainbow
Used to test the rainbow cycle of series neopixel LED 

## flash firmware

`esptool.py --chip esp32s2 --port /dev/ttyACM0 --baud 460800 --before default_reset --after no_reset write_flash -z 0x1000 firmware.bin`