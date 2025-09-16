import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
photo = 6
GPIO.setup(photo, GPIO.IN)
state = 0
while True:
    if GPIO.input(photo) == 0:
        GPIO.output(led, 0)
    else:
        GPIO.output(led, 1)