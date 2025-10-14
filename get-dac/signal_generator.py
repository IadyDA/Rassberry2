import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    be = np.sin(2*np.pi*freq*time)
    be1 = be + 1 #сдвинули область значений
    be2 = be1/2
    return be2

def wait_for_sampling_period(samp_freq):
    T = 1 / samp_freq
    time.sleep(T)