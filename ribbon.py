import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm
import colormaps as cmaps


j = 1
for i in range(1, 61, 10):

    rc = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv', delimiter=',', skip_header=1)
    r = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_curv{j}.csv', delimiter=',', skip_header=1)
    tau = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240427 Twist Rate, Ribbon Frame {j}/twist_rate_ribbon{j}_time{i}.csv')

    rc = rc[1:99, :]
    r = r[1:99, :]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    triangles = []
    color_map = []

    for ii in range(len(rc) - 1):
        p1 = rc[ii]
        p2 = rc[ii + 1]
        p3 = r[ii + 1]
        p4 = r[ii]

        triangles.append([p1, p2, p3])
        color_map.append(tau[ii])
        triangles.append([p1, p3, p4])
        color_map.append(tau[ii])

    # Normalize color_map manually
    norm = plt.Normalize(vmin=-0.7, vmax=0.7)
    cmap = cmaps.berlin
    normalized_colors = cmap(norm(color_map))

    # Create a Poly3DCollection
    tri_collection = Poly3DCollection(triangles, facecolors=normalized_colors)

    # Add to axis
    ax.add_collection3d(tri_collection)

    # Setting the same scale for all axes
    max_range = 140
    mid_x = (250 + -50) / 2.0
    mid_y = (100 + -100) / 2.0
    mid_z = (100 + -100) / 2.0

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # Add a color bar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, pad=0.1)
    cbar.set_label('Twist Rate')

    fig.suptitle(f'Ribbon {j}, Time {i}')
    plt.savefig(f'ribbon{j}_time{i:02}_norm.png')
    plt.show()
    plt.close(fig)
