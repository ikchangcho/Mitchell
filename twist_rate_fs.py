# Calculate the twist rate of a curve in the Frenet-Serret frame

import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab

# Import coordinates of points on the center line
for i in range(1, 61):
    x = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv',
                      delimiter=',', skip_header=1)

    d3 = np.zeros((99, 3))   # Tangent vector
    d1 = np.zeros((98, 3))   # Normal vector
    K = np.zeros(98)        # Curvature
    d2 = np.zeros((98, 3))   # Binormal vector
    tau = np.zeros(97)      # Twist rate, Torsion

    for n in range(99):
        d3[n] = (x[n + 1] - x[n])
        d3[n] = d3[n] / np.linalg.norm(d3[n])

    for n in range(98):
        d1[n] = d3[n + 1] - d3[n]
        K[n] = np.linalg.norm(d1[n])
        d1[n] = d1[n] / K[n]
        d2[n] = np.cross(d3[n], d1[n])

    for n in range(97):
        tau[n] = (-1) * np.inner(d1[n], d2[n + 1] - d2[n])

    # Plot Centerline in 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(x[1:98, 0], x[1:98, 1], x[1:98, 2], c=tau, cmap=plt.cm.RdBu)
    cbar = plt.colorbar(sc, ax=ax, shrink=0.5, aspect=10)
    cbar.set_label('Twist Rate')

    # Setting the same scale for all axes
    max_range = np.array([x[1:98, 0].max()-x[1:98, 0].min(), x[1:98, 1].max()-x[1:98, 1].min(), x[1:98, 2].max()-x[1:98, 2].min()]).max() / 2.0

    mid_x = (x[1:98, 0].max()+x[1:98, 0].min()) * 0.5
    mid_y = (x[1:98, 1].max()+x[1:98, 1].min()) * 0.5
    mid_z = (x[1:98, 2].max()+x[1:98, 2].min()) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    ax.set_title(f'Centerline, Time {i}')
    plt.savefig(f'centerline_fs_{i}.png', bbox_inches='tight')
    plt.close(fig)

    # # Plot Twist Rate
    # fig, ax = plt.subplots(figsize=(10, 8))
    # ax.plot(tau)
    # ax.set_xlabel('s')
    # ax.set_ylabel(r'$\tau(s)$')
    # ax.set_title(f'Twist Rate in the Frenet-Serret Frame, Time {i}')
    # plt.savefig(f'twist_rate_fs_{i}.png', bbox_inches='tight')
    # plt.close(fig)