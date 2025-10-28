import RPi.GPIO as GPIO
import time
# import matplotlib.pyplot as plt
import r2r_adc as r2r
import adc_plot as plt

adc = r2r.R2R_ADC(3.3, compare_time = 0.01, verbose = False)

voltage_values = []
time_values = []
duration = 3.0

if __name__ == '__main__':
    try:
        start_time = time.time()
        current_time = time.time()

        while current_time - start_time < duration:
            voltage_values.append(adc.get_sc_voltage())
            time_values.append(current_time - start_time)
            current_time = time.time()
        
        plt.plot_voltage_vs_time(time_values, voltage_values, 3.3)
        plt.plot_sampling_period_hist(time_values)

    finally:
        adc.deinit()
