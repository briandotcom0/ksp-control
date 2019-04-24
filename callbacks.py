import RPi.GPIO as GPIO
import pins
import krpc
import krpc

conn
vessel

def setup(c,v):
    conn=c
    vessel=v

def rcs(channel):
    vessel.control.rcs=GPIO.input(channel)
    GPIO.output(pins.rcsout,GPIO.input(channel))

def sas(channel):
    vessel.control.sas=GPIO.input(channel)
    GPIO.output(pins.sasout,GPIO.input(channel))