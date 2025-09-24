import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

    GPIO.setup(21,GPIO.OUT)

def led_on(time_on):
    print("working")

    print("led on")
    GPIO.output(21,GPIO.HIGH)
    sleep(time_on)
    GPIO.output(21,GPIO.LOW)

