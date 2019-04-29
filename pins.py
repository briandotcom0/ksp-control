import RPi.GPIO as GPIO

class Pins:
    rcsin = 3
    rcsout = 4
    sasin=5
    sasout=6
    gearin=7
    gearout=8
    brakes=9
    solar=10
    rotA1=11
    rotA2=12
    rotB1=13
    rotB2=14

    lights=[rcsout, sasout, gearout]
    rots=[rotA1, rotA2, rotB1, rotB2]
    calls=None
    single=None

    def setup(self, callback, s):
        self.calls=callback
        self.single=s
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.rcsin, GPIO.IN)
        GPIO.setup(self.sasin, GPIO.IN)
        GPIO.setup(self.lights, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.gearin, GPIO.IN)
        GPIO.setup(self.brakes, GPIO.IN)
        GPIO.setup(self.solar, GPIO.IN)
        GPIO.setup(self.rots, GPIO.IN)

        GPIO.add_event_callback(self.rcsin, self.calls.rcs, bouncetime=100)
        GPIO.add_event_callback(self.sasin, self.calls.sas, bouncetime=100)
        GPIO.add_event_callback(self.gearin, self.calls.gear, bouncetime=100)
        GPIO.add_event_callback(self.solar, self.calls.solar, bouncetime=100)
        GPIO.add_event_callback(self.brakes, self.calls.brakes)
        GPIO.add_event_callback(self.rotA1, self.calls.rotA, bouncetime=10)
        GPIO.add_event_callback(self.rotB1, self.calls.rotB, 10)
        GPIO.add_event_callback(self.rotA2, self.calls.rotA, bouncetime=10)
        GPIO.add_event_callback(self.rotB2, self.calls.rotB, 10)

    def cleanup(self):
        GPIO.cleanup(self.lights)
        GPIO.cleanup(self.rots)
        GPIO.cleanup([self.rcsin, self.sasin, self.gearin, self.solar, self.brakes])
