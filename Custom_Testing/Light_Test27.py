#!/usr/bin/env python3
from gpiozero import LED
from time import sleep

print ('Program is starting ... ')

led = LED(27)           # define LED pin according to BCM Numbering
# led = LED("J8:11")     # BOARD Numbering
'''
# pins numbering, the following lines are all equivalent
led = LED("GPIO17")     # BCM
led = LED("BCM17")      # BCM
led = LED("BOARD11")    # BOARD
led = LED("WPI0")       # WiringPi
led = LED("J8:11")      # BOARD
'''

while True:
    print("Light on")
    led.on()    # turn on LED
