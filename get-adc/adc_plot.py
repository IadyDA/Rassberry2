import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.title('График зависимости напряжения на входе АЦП от времени')
    plt.grid()
    plt.show()