import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Import coordinates of points on the center line
i = 1
r = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv',
                  delimiter=',', skip_header=1)

# Smooth positions by using the Savitzky-Golay filter
# To increase the amount of smoothing we have to increase the ratio w/p
w = 20
p = 2
r_smooth = savgol_filter(r, w, polyorder=p, axis=0, mode='nearest')
r_smooth_der1 = savgol_filter(r, w, polyorder=p, axis=0, mode='nearest', deriv=1)
norms_der1 = np.linalg.norm(r_smooth_der1, axis=1, keepdims=True)

# Define the Frenet-Serret frame
d3 = r_smooth_der1 / norms_der1     # Tangent vectors
d1 = savgol_filter(d3, w, polyorder=p, axis=0, mode='nearest', deriv=1)
d1 = d1 / np.linalg.norm(d1, axis=1, keepdims=True)
d2 = np.cross(d3, d1, axis=1)

# Define the Frenet-Serret frame by taking discrete differentiation
d33 = np.zeros((99, 3))
for n in range(99):
    d33[n] = (r[n + 1] - r[n])
    d33[n] = d33[n] / np.linalg.norm(d33[n])
d11 = np.zeros((98, 3))
for n in range(98):
    d11[n] = d3[n + 1] - d3[n]
    d11[n] = d11[n] / np.linalg.norm(d11[n])

# Check the smoothness of the normal vectors
print("Smoothness Savitzky-Golay")
for j in range(1, 11):
    print(np.inner(d1[j+1,:], d1[j,:]))
print("Smoothness Discrete")
for j in range(1, 11):
    print(np.inner(d11[j+1,:], d11[j,:]))

# Check the orthoganlity between the normal vectors and the tangent vectors
print("Orthogonality Savitzky-Golay")
for j in range(1, 11):
    print(np.inner(d3[j,:], d1[j,:]))
print("Orthogonality Discrete")
for j in range(1, 11):
    print(np.inner(d33[j,:], d11[j,:]))
