# RP2040 upython program
# Read inputs from TT02 board
from machine import Pin
import utime

# Pins mapping
# Pin   Label  Function
# 19    in0    GPIO14
# 20    in1    GPIO15
# 21    in2    GPIO16
# 22    in3    GPIO17
# 24    in4    GPIO18
# 25    in5    GPIO19
# 26    in6    GPIO20
# 27    in7    GPIO21

# 12    out0   GPIO9
# 11    out1   GPIO8
# 10    out2   GPIO7
# 9     out3   GPIO6
# 29    out4   GPIO22
# 31    out5   GPIO26
# 32    out6   GPIO27
# 34    out7   GPIO28

OUT_PINS = [28, 27, 26, 22, 6, 7, 8, 9]  # List of out pin numbers
IN_PINS = [21, 20, 19, 18, 17, 16, 15, 14]  # List of in pin numbers

IN_RES = 15 # In reset
TrainLED_PIN = 16  # (in2)
slow_clock = 2454 # 12 TrainLED clockcycles per WS2812 bit
zero_len_us = int(1e6*4.0/slow_clock)
one_len_us = int(1e6*8.0/slow_clock)

# The clock rate of TrainLED is too slow for a PIO based WS2812 implementation, hence we use a software bit-banging approach
# to send the bits to the TrainLED. The following function sends a byte to the TrainLED using the given pin.

def send_byte_TrainLED(pin, byte):
    for i in range(8):
        if byte & 0x80:
            # Send 1
            pin.on()
            utime.sleep_us(one_len_us)
            pin.off()
            utime.sleep_us(zero_len_us)
        else:
            # Send 0
            pin.on()
            utime.sleep_us(zero_len_us)
            pin.off()
            utime.sleep_us(one_len_us)            
        byte <<= 1

def initialize_gpio():
    # Initialize in pins  GPIO as input
    for pin in IN_PINS:
        Pin(pin, Pin.IN)

    # Initialize out pins GPIO as input
    for pin in OUT_PINS:
        Pin(pin, Pin.IN)

def read_in_pins():
    # Read in pins and combine into a byte
    byte = 0
    for pin in IN_PINS:
        value = Pin(pin, Pin.IN).value()
        byte = (byte << 1) | value

    return byte

def read_out_pins():
    # Read out pins and combine into a byte
    byte = 0
    for pin in OUT_PINS:
        value = Pin(pin, Pin.IN).value()
        byte = (byte << 1) | value

    return byte

initialize_gpio()

def set_res(res):
    # Set the clock to high or low
    Pin(IN_RES, Pin.OUT).value(res)

# print timing
print("Timing one bit: ", one_len_us, "us")    
print("Timing zero bit: ", zero_len_us, "us")

# reset

set_res(0)
utime.sleep_ms(100)
set_res(1)
utime.sleep_ms(100)
set_res(0)


while True:
    send_byte_TrainLED(Pin(TrainLED_PIN, Pin.OUT), 0x10)
    send_byte_TrainLED(Pin(TrainLED_PIN, Pin.OUT), 0x40)
    send_byte_TrainLED(Pin(TrainLED_PIN, Pin.OUT), 0xf0)

    utime.sleep_ms(500)

    send_byte_TrainLED(Pin(TrainLED_PIN, Pin.OUT), 0xf0)
    send_byte_TrainLED(Pin(TrainLED_PIN, Pin.OUT), 0xc0)
    send_byte_TrainLED(Pin(TrainLED_PIN, Pin.OUT), 0x10)
    utime.sleep_ms(500)
