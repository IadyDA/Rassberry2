import r2r_dac as r2r
import signal_generator as sg
import time
import RPi.GPIO as GPIO
from signal_generator import get_sin_wave_amplitude
from signal_generator import wait_for_sampling_period

a = 3.2
freq = 10
samp_freq = 1000

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        self.number = number
        bins = [int(element) for element in bin(self.number)[2:].zfill(8)]
        i=0
        for bit in self.gpio_bits:
            GPIO.output(bit, bins[i])
            i+=1

    def set_voltage(self, voltage):
        self.voltage = voltage
        self.set_number(int(self.voltage))

    def voltage_to_number(self, voltage):
        self.voltage = voltage
        if not (0.0 <= self.voltage <= self.dynamic_range):
            print(f'Напряжение выходит за динамический диапазон ЦАП(0,00 - {self.dynamic_range} В')
            print('Устанавливаем 0.0 В')
            return 0
    
        return int(self.voltage / self.dynamic_range * 255)

t=0.5

if __name__ == '__main__':
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                A = get_sin_wave_amplitude(freq, t)
                number = dac.voltage_to_number(A)
                dac.set_voltage(number)
                t+=0.5
                wait_for_sampling_period(samp_freq)
                print(t, A)
            
            except ValueError:
                print('Вы ввели не число. Попробуйте ещё раз\n')

    finally:
        dac.deinit()