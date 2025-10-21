import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        self.number = number
        bins = [int(element) for element in bin(self.number)[2:].zfill(8)]
        i=0
        for bit in self.bits_gpio:
            GPIO.output(bit, bins[i])
            i+=1

    def sequential_counting_adc(self):
        for i in range(256):
            number_to_dac(i)
            time.sleep(0.01)
            if GPIO.input(self.comp_gpio):
                print(i)
                i = 256
            if i == 255 and not(GPIO.input(self.comp_gpio)):
                print(i)

    def get_sc_voltage(self):
        for m in range(256):
            return int(m / self.dynamic_range * 255)


if __name__ == '__main__':
    try:
        dac = R2R_ADC(3.3, compare_time = 0.01, verbose = False)

        while True:
            try:
                sequential_counting_adc()

            except ValueError:
                print('Вы ввели не число. Попробуйте ещё раз\n')

    finally:
        dac.deinit()

