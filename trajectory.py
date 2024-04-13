import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab

# Import coordinates of points on the center line
i = 60
r = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv',
                  delimiter=',', skip_header=1)

d3 = np.zeros((99, 3))   # Tangent vector
d1 = np.zeros((98, 3))   # Normal vector
K = np.zeros(98)        # Curvature
d2 = np.zeros((98, 3))   # Binormal vector
tau = np.zeros(97)      # Twist rate, Torsion

for n in range(99):
    d3[n] = (r[n + 1] - r[n])
    d3[n] = d3[n] / np.linalg.norm(d3[n])

for n in range(98):
    d1[n] = d3[n + 1] - d3[n]
    K[n] = np.linalg.norm(d1[n])
    d1[n] = d1[n] / K[n]
    d2[n] = np.cross(d3[n], d1[n])

for n in range(97):
    tau[n] = (-1) * np.inner(d1[n], d2[n + 1] - d2[n])

# # Matplotlib
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
# sc = ax.scatter(r[1:98, 0], r[1:98, 1], r[1:98, 2], c=tau, cmap=plt.cm.RdBu)
# cbar = plt.colorbar(sc, ax=ax, shrink=0.5, aspect=10)
#
# plt.title(f'Time {i}')
# plt.tight_layout()
# plt.show()

# Mayavi
x = r[1:98, 0]
y = r[1:98, 1]
z = r[1:98, 2]

mlab.figure(bgcolor=(1, 1, 1))  # Optional: set background to white for better visibility
from matplotlib.colors import ListedColormap
custom_cmap = ListedColormap(['red', 'blue'])
line = mlab.plot3d(x, y, z, tau, tube_radius=1.0, colormap='coolwarm')  # Tube radius is optional for aesthetic thickness of the line
colorbar = mlab.colorbar(line, title='Twist Rate', orientation='vertical')
mlab.show()