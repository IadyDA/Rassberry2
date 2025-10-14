import r2r_dac as r2r
import signal_generator as sg
import time
import RPi.GPIO as GPIO

a = 3.2
freq = 10
samp_freq = 1000

if __name__ == '__main__':
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

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