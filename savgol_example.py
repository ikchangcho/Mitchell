import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

data = np.genfromtxt('centerline.csv', delimiter=',', skip_header=1)
X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]
S = np.arange(1, 101)

w = 5
p = 2
data_smooth = savgol_filter(data, w, polyorder=p, axis=0, mode='nearest')
data_smooth_div1 = savgol_filter(data, w, polyorder=p, axis=0, deriv=1)
Z_smooth = data_smooth[:,2]
Z_smooth_div1 = data_smooth_div1[:,2]
interval = np.arange(0,21)

plt.scatter(S[interval], Z[interval], s=20)
plt.plot(S[interval], Z_smooth[interval], color='red')
plt.plot(S[interval], Z_smooth_div1[interval], color='red')
plt.show()

