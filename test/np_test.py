import esp32, machine, time

# The channel resolution is 100ns (1/(source_freq/clock_div)).
r = esp32.RMT(0, pin=machine.Pin(18), clock_div=8)

def np_data(pixel):
    np_bits = ((3, 8), (8, 8)) # 300ns, 800ns, 800ns, 800ns
    data = ()
    for bit in range(24):
        data += np_bits[(pixel >> (23-bit)) & 1]
    return data

clear = np_data(0x00_00_00) * 25
r.write_pulses(clear, 1)
time.sleep_us(1000) # RESET LED
all_green = np_data(0x00_0A_00) * 20
r.write_pulses(all_green, 1)
out4 = np_data(0x00_00_03) * 10
start = time.ticks_ms()
while 1:
    delta = time.ticks_diff(time.ticks_ms(), start)
    time.sleep_us(800) # RESET LED
    r.write_pulses(out4, 1)
    if delta > 2000:
        r.write_pulses(clear, 1)
        time.sleep_us(800)
        r.write_pulses(all_green, 1)
        start = time.ticks_ms()