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

    def voltage_to_number(self, voltage):
        self.voltage = voltage
        if not (0.0 <= self.voltage <= self.dynamic_range):
            print(f'Напряжение выходит за динамический диапазон ЦАП(0,00 - {self.dynamic_range} В')
            print('Устанавливаем 0.0 В')
            return 0
    
        return int(self.voltage / self.dynamic_range * 255)

if __name__ == '__main__':
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input('Введите напряжение в Вольтах: '))
                number = dac.voltage_to_number(voltage)
                dac.set_voltage(number)
            
            except ValueError:
                print('Вы ввели не число. Попробуйте ещё раз\n')

    finally:
        dac.deinit()