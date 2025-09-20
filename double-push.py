import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24] #все светяшки
GPIO.setup(leds, GPIO.OUT) #настроили выход на светяшки
GPIO.output(leds, 0) #погасили все светяшки

buttons = [9, 10]
GPIO.setup(buttons, GPIO.IN)

up = 9
down = 10

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if num < 0 or num > 256:
        break
    if GPIO.input(up):
        num = num + 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    if GPIO.input(down):
        num = num - 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    if GPIO.input(up) and GPIO.input(down):
        num = 255
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    i = 0
    for led in leds:
            GPIO.output(led, dec2bin(num)[i])
            i+=1