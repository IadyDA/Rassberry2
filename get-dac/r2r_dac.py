import RPi.GPIO as GPIO


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

if __name__ == '__main__':
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input('Введите напряжение в Вольтах: '))
                dac.set_voltage(voltage)
            
            except ValueError:
                print('Вы ввели не число. Попробуйте ещё раз\n')

    finally:
        dac.deinit()