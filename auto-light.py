import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
photo = 6

GPIO.setup(photo, GPIO.IN)
while True:
    if GPIO.input(photo):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)