import RPi.GPIO as GPIO
from time import sleep


def led_on(time_on):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(21,GPIO.OUT)

    print("led on")
    GPIO.output(21,GPIO.HIGH)
    sleep(time_on)
    GPIO.output(21,GPIO.LOW)

