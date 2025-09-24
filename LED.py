import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

GPIO.setup(21,GPIO.OUT)

print("led on")
GPIO.output(21,GPIO.HIGH)
sleep(1)
GPIO.output(21,GPIO.LOW)

