import pwm_dac
import signal_generator as sg
import time

a = 3.2
freq = 10
samp_freq = 1000

try:
    dac = pwm_dac.PWM_DAC(12, 500, 3.290, True)
    while True:
        try:
            start_time = time.time()
            A = a * sg.get_sin_wave_amplitude(freq, start_time)
            number = dac.voltage_to_number(A)
            dac.set_voltage(number)
            sg.wait_for_sampling_period(samp_freq)
            print(start_time, A)

        except ValueError:
            print('Вы ввели не число. Попробуйте ещё раз\n')

finally:
        dac.deinit()