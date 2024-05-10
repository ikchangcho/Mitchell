from spherical_triangle import *
import numpy as np
import matplotlib.pyplot as plt

tp = 60
data = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{tp:06}_centerline.csv', delimiter=",", skip_header=1)
tangents = np.zeros((99, 3))
new_writhe_density = np.zeros(97)

for i in range(99):
    tangents[i] = data[i+1] - data[i]
    tangents[i] = tangents[i] / np.linalg.norm(tangents[i])

for i in range(97):
    new_writhe_density[i] = spherical_area(tangents[i], tangents[i+1], tangents[i+2]) * sign_of_area(tangents[i], tangents[i+1], tangents[i+2])

fig, ax = plt.subplots()

ax.plot(np.cumsum(new_writhe_density))
ax.set_ylim()
plt.show()