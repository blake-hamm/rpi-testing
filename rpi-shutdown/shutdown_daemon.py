import os
from subprocess import check_call
import time

import daemon
from gpiozero import DigitalOutputDevice, DigitalInputDevice

class Monitor:

    def __init__(self, ac_pin="GPIO17", power_pin="GPIO22", timer_pin="GPIO27"):
        
        print("Connecting to pins")

        self._check_ac = DigitalInputDevice(ac_pin)
        self._trigger_power = DigitalOutputDevice(power_pin)
        self._trigger_power.on()
        self._trigger_timer = DigitalOutputDevice(timer_pin)

    def _shutdown():
        check_call(['sudo', 'poweroff'])

    def check(self):
        if self._check_ac.is_active:
            print("No Accessory - shutdown initialized")
            self._trigger_timer.on()
            time.sleep(1)
            self._trigger_timer.off()
            print("No Accessory - timer relay toggled")
            time.sleep(1)
            self._trigger_power.off()
            print("No Accessory - main power relay off")
            print("Waiting 40 seconds for shutdown...")
            self._shutdown()
            time.sleep(40)
        else:
            time.sleep(1)
            print("Accessory Detected")
        

def rpi_monitor():
    monitor = Monitor()
    while True:
        monitor.check()

if __name__ == "__main__":
    logs = "/var/log"
    out = open('shutdown_daemon.log', 'w+')

    with daemon.DaemonContext(working_directory=logs, stdout=out):
        rpi_monitor()