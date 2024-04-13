import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab

# Import coordinates of points on the center line
tau1 = np.zeros((60, 97))
tau2 = np.zeros((60, 97))

for i in range(1, 60):
    x = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv',
                      delimiter=',', skip_header=1)

    d3 = np.zeros((99, 3))   # Tangent vector
    d1 = np.zeros((98, 3))   # Normal vector
    K = np.zeros(98)        # Curvature
    d2 = np.zeros((98, 3))   # Binormal vector

    for n in range(99):
        d3[n] = (x[n + 1] - x[n])
        d3[n] = d3[n] / np.linalg.norm(d3[n])

    for n in range(98):
        d1[n] = d3[n + 1] - d3[n]
        K[n] = np.linalg.norm(d1[n])
        d1[n] = d1[n] / K[n]
        d2[n] = np.cross(d3[n], d1[n])

    for n in range(97):
        tau1[i-1, n] = (-1) * np.inner(d1[n], d2[n + 1] - d2[n])

for i in range(1, 60):
    x = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i+1:06}_centerline.csv',
                      delimiter=',', skip_header=1)

    d3 = np.zeros((99, 3))   # Tangent vector
    d1 = np.zeros((98, 3))   # Normal vector
    K = np.zeros(98)        # Curvature
    d2 = np.zeros((98, 3))   # Binormal vector

    for n in range(99):
        d3[n] = (x[n + 1] - x[n])
        d3[n] = d3[n] / np.linalg.norm(d3[n])

    for n in range(98):
        d1[n] = d3[n + 1] - d3[n]
        K[n] = np.linalg.norm(d1[n])
        d1[n] = d1[n] / K[n]
        d2[n] = np.cross(d3[n], d1[n])

    for n in range(97):
        tau2[i-1, n] = (-1) * np.inner(d1[n], d2[n + 1] - d2[n])

tauderv = tau2 - tau1

# Plot Twist Rate
i = 0
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(tauderv[i])
ax.set_xlabel('s')
ax.set_ylabel(r'$\tau(s)$')
ax.set_title(f'Derivative of Twist Rate in the Frenet-Serret Frame, Time {i+1}')
#plt.savefig(f'twist_rate_fs_{i}.png', bbox_inches='tight')
plt.show()
plt.close(fig)

