import mcp4725_driver as mcp
import signal_generator as sg
import time

a = 3.2
freq = 10
samp_freq = 1000

try:
    dac = mcp.MCP4725(5.11, address = 0x61, verbose = True)

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