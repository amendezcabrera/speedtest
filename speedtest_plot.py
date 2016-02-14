import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

def read_datafile(file_name):
    # the skiprows keyword is for heading, but I don't know if trailing lines
    # can be specified
    data = np.loadtxt(file_name, delimiter=',', skiprows=10)
    return data

data_csv_file = "/home/alberto/Desarrollo/Proyectos/Scripts/SpeedTest/data.csv"

data = np.genfromtxt(data_csv_file, delimiter=',', skip_header=10,
                     skip_footer=10, names=['x', 'y', 'z'])

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Mains power stability")
ax1.set_xlabel('time')
ax1.set_ylabel('Mains voltage')

ax1.plot(data['x'], data['y'], color='r', label='the data')

leg = ax1.legend()

plt.show()
