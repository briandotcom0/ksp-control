import RPi.GPIO as GPIO
import pins
import singleton
# import krpc  #???

# conn= None
vessel= None

def init():
    vessel=singleton.getVessel()
    pins.setup()

def rcs(channel):
    vessel.control.rcs=GPIO.input(channel)
    GPIO.output(pins.rcsout, GPIO.input(channel))

def sas(channel):
    vessel.control.sas=GPIO.input(channel)
    GPIO.output(pins.sasout, GPIO.input(channel))
