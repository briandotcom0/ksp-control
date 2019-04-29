import RPi.GPIO as GPIO
# import krpc  #???


class Callbacks:
    # conn= None
    vessel= None
    rotAl = None
    rotBl = None
    pin = None
    single = None

    def init(self, s, p):
        single=s
        self.vessel=single.getVessel()
        pin=p
        pin.setup(self, s)
        self.rotAl=[GPIO.input(pin.rotA1), GPIO.input(pin.rotA2)]
        self.rotBl=[GPIO.input(pin.rotB1), GPIO.input(pin.rotB2)]

    def rcs(self, channel):
        self.vessel.control.rcs=GPIO.input(channel)
        GPIO.output(self.pin.rcsout, GPIO.input(channel))

    def sas(self, channel):
        self.vessel.control.sas=GPIO.input(channel)
        GPIO.output(self.pin.sasout, GPIO.input(channel))

    def gear(self, channel):
        self.vessel.control.gear=GPIO.input(channel)
        GPIO.output(self.pin.gearout, GPIO.input(channel))

    def solar(self, channel):
        self.vessel.control.radiators=GPIO.input(channel)
        self.vessel.control.solar_panels=GPIO.input(channel)

    def brakes(self, channel):
        self.vessel.control.brakes=GPIO.input(channel)

    def rotAhandle(self, direction):
        if direction == GPIO.HIGH:
            print("A -> right")
        else:
            print("A -> left")

    def rotBhandle(self, direction):
        if direction == GPIO.HIGH:
            print("B -> right")
        else:
            print("B -> left")

    def rotA(self, channel):
        if channel==self.pin.rotA1:
            if self.rotAl[0]==GPIO.HIGH:
                self.rotAhandle(self.rotAl[1])
            else:
                if self.rotAl[1] == GPIO.HIGH:
                    self.rotAhandle(GPIO.LOW)
                else:
                    self.rotAhandle(GPIO.HIGH)
            self.rotAl[0]=GPIO.input(channel)
        else:
            if self.rotAl[0]==GPIO.HIGH:
                if self.rotAl[1] == GPIO.HIGH:
                    self.rotAhandle(GPIO.LOW)
                else:
                    self.rotAhandle(GPIO.HIGH)
            else:
                self.rotAhandle(self.rotAl[1])
            self.rotAl[1]=GPIO.input(channel)


    def rotB(self, channel):
        if channel==self.pin.rotB1:
            if self.rotBl[0]==GPIO.HIGH:
                self.rotBhandle(self.rotBl[1])
            else:
                if self.rotBl[1] == GPIO.HIGH:
                    self.rotBhandle(GPIO.LOW)
                else:
                    self.rotBhandle(GPIO.HIGH)
            self.rotBl[0]=GPIO.input(channel)
        else:
            if self.rotBl[0]==GPIO.HIGH:
                if self.rotBl[1] == GPIO.HIGH:
                    self.rotBhandle(GPIO.LOW)
                else:
                    self.rotBhandle(GPIO.HIGH)
            else:
                self.rotBhandle(self.rotBl[1])
            self.rotBl[1]=GPIO.input(channel)\
