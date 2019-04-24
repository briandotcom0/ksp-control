import RPi.GPIO as GPIO
import pins
# import krpc  #???

conn=0
vessel=0

def setup(c,v):
    conn=c
    vessel=v
    pins.setup()

def rcs(channel):
    vessel.control.rcs=GPIO.input(channel)
    GPIO.output(pins.rcsout, GPIO.input(channel))

def sas(channel):
    vessel.control.sas=GPIO.input(channel)
    GPIO.output(pins.sasout, GPIO.input(channel))
