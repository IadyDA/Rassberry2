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

    def dec2bin(self, value):
        self.value = value
        return [int(element) for element in bin(self.value)[2:].zfill(8)]

    def number_to_dac(self, number):
        self.number = number
        bins = self.dec2bin(self.number)
        i=0
        for bit in self.bits_gpio:
            GPIO.output(bit, bins[i])
            i+=1

    def sequential_counting_adc(self):
        for i in range(256):
            self.number_to_dac(i)
            if GPIO.input(self.comp_gpio) != 0:
                break
        time.sleep(self.compare_time)
        return i

    def get_sc_voltage(self):
        return self.sequential_counting_adc() / 255 * self.dynamic_range


if __name__ == '__main__':
    try:
        adc = R2R_ADC(3.3, compare_time = 0.01, verbose = False)

        while True:
            try:
                u = adc.get_sc_voltage()
                print(u)

            except ValueError:
                print('Вы ввели не число. Попробуйте ещё раз\n')

    finally:
        adc.deinit()

