# RP2040 upython program
# Measure slow clock frequency, slow clock must be connected to GPIO10

from machine import Pin
import utime

# slow clock pin mapping
SLOW_CLK_PIN = 10  # GPIO10

# Global counter
counter = 0

# Interrupt handler for rising edges
def on_rising(clkpin):
    global counter
    counter += 1

# Setup GPIO pin
clkpin = Pin(SLOW_CLK_PIN, Pin.IN, Pin.PULL_DOWN)
clkpin.irq(trigger=Pin.IRQ_RISING, handler=on_rising)

print("Measuring... (wait 5 seconds)")

counter = 0
waittime = 5 
utime.sleep_ms(1000*waittime)  # Wait for 1 second, simulate rising edge externally
readcounter = counter

print("Slow clock frequency: ", readcounter / waittime, "Hz")

