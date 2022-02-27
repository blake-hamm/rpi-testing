from gpiozero import DigitalOutputDevice
import time

output_pin = DigitalOutputDevice("GPIO22")

output_pin.on()

time.sleep(10)

output_pin = DigitalOutputDevice("GPIO21")

output_pin.on()

time.sleep(2)