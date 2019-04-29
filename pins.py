import RPi.GPIO as GPIO
import callbacks


rcsin = 3
rcsout = 4
sasin=5
sasout=6

lights=[rcsout, sasout]

def setup():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(rcsin, GPIO.IN)
    GPIO.setup(sasin, GPIO.IN)
    GPIO.setup(lights, GPIO.OUT, initial=GPIO.LOW)

    GPIO.add_event_callback(rcsin, callbacks.rcs, bouncetime=100)
    GPIO.add_event_callback(sasin, callbacks.sas, bouncetime=100)

def cleanup():
    GPIO.cleanup(lights)
    GPIO.cleanup([rcsin, sasin])
