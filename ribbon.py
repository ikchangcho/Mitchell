import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm
import colormaps as cmaps

j = 1
for i in range(1, 61):

    rc = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv', delimiter=',', skip_header=1)
    r = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_curv{j}.csv', delimiter=',', skip_header=1)
    tau = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240427 Twist Rate, Ribbon Frame {j}/twist_rate_ribbon{j}_time{i}.csv')

    rc = rc[1:99, :]
    r = r[1:99, :]

    threshold = 0.3
    over_saturated = (np.abs(tau) > threshold).sum()
    cmap = cm.RdBu_r

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.text(300, -100, -170,f'Oversaturated: {over_saturated}/{len(tau)}', size=10)

    # Set the colors of each axis pane
    ax.xaxis.pane.fill = True  # Ensure the pane is filled
    ax.yaxis.pane.fill = True
    ax.zaxis.pane.fill = True

    ax.xaxis.pane.set_facecolor('black')  # Set x-axis plane color
    ax.yaxis.pane.set_facecolor('black')  # Set y-axis plane color
    ax.zaxis.pane.set_facecolor('black')  # Set z-axis plane color

    # Change the grid color and style
    ax.xaxis._axinfo["grid"].update(color='black', linewidth=0.1)
    ax.yaxis._axinfo["grid"].update(color='black', linewidth=0.1)
    ax.zaxis._axinfo["grid"].update(color='black', linewidth=0.1)

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
    norm = plt.Normalize(vmin=-threshold, vmax=threshold)
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
    cbar.set_label('Twist Rate', fontsize=15, rotation=270, labelpad=15)

    fig.suptitle(f'Ribbon Frame {j}, Time {i:02}', fontsize=20, fontweight='bold')
    plt.savefig(f'/Users/ik/Pycharm/Mitchell/240428 Ribbon {j}, Threshold {threshold}/ribbon{j}_time{i:02}_thrsh{threshold}.png')
    plt.show()
    plt.close(fig)
