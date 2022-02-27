from gpiozero import DigitalOutputDevice, DigitalInputDevice

class RelayMonitor:
    def __init__(self, send_pin, read_pin, con_type="NC"):
        print("Connecting to pins")
        self.Send = DigitalOutputDevice(send_pin)
        self.Read = DigitalInputDevice(read_pin)

        if con_type == "NC":
            self.active_message = "No signal"
            self.deactive_message = "Signal Detected"
        else:
            self.active_message = "Signal Detected"
            self.deactive_message = "No signal"


    def monitor(self):
        print("Starting Program")

        self.Send.on()

        while True:
            if self.Read.is_active:
                print(self.active_message)
            else:
                print(self.deactive_message)


## Test:
test = RelayMonitor("GPIO17", "GPIO27")

test.monitor()