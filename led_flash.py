import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21,GPIO.OUT)

def led_on():
    GPIO.output(21,GPIO.HIGH)

def led_off():
    GPIO.output(21,GPIO.LOW)

