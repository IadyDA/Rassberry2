import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        self.voltage = voltage
        self.pwm.ChangeDutyCycle(self.voltage)

    def voltage_to_number(self, voltage):
        self.voltage = voltage
        if not (0.0 <= self.voltage <= self.dynamic_range):
            print(f'Напряжение выходит за динамический диапазон ЦАП(0,00 - {self.dynamic_range} В')
            print('Устанавливаем 0.0 В')
            return 0
        return int(self.voltage / self.dynamic_range * 100)
            

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                number = dac.voltage_to_number(voltage)
                dac.set_voltage(number)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()