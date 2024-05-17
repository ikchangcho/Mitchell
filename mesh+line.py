'''Generate a 3D line plot of a curve with mesh'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import colormaps as cmaps
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

torsions = np.genfromtxt("CSV/torsion.csv", delimiter=",", skip_header=1)
for i in range(1, 2):
    rc = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv', delimiter=',', skip_header=1)
    r1 = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_curv1.csv', delimiter=",", skip_header=1)
    r2 = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 curves, Centerlines (Resampled to 100)/tp{i:06}_curv2.csv', delimiter=",", skip_header=1)
    r3 = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_curv3.csv', delimiter=",", skip_header=1)
    r4 = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_curv4.csv', delimiter=",", skip_header=1)
    tau = torsions[i]
    cmap = cmaps.berlin
    L = len(tau)

    # Assuming `r` and `tau` are defined and `cmap` is set
    fig = plt.figure(figsize=(20, 15))
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.plot(r1[:, 0], r1[:, 1], r1[:, 2], label='Ribbon1')
    ax.plot(r2[:, 0], r2[:, 1], r2[:, 2], label='Ribbon2')
    ax.plot(r3[:, 0], r3[:, 1], r3[:, 2], label='Ribbon3')
    ax.plot(r4[:, 0], r4[:, 1], r4[:, 2], label='Ribbon4')

    # # Prepare the points to plot
    # points = rc[1:L + 1, :].reshape(-1, 1, 3)
    # segments = np.concatenate([points[:-1], points[1:]], axis=1)
    #
    # # Create a Line3DCollection
    # lc = Line3DCollection(segments, cmap=cmap, norm=plt.Normalize(vmin=-1.3, vmax=1.3))
    # lc.set_array(tau)  # Set the colors according to tau

    # # Add collection to the axes
    # ax.add_collection3d(lc)

    # Setting the same scale for all axes
    max_range = 140
    mid_x = (250 + -50) / 2.0
    mid_y = (100 + -100) / 2.0
    mid_z = (100 + -100) / 2.0

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # # Adding a color bar
    # cb = fig.colorbar(lc, ax=ax, pad=0.1)
    # cb.set_label('Twist Rate')

    # Load data
    vertices = pd.read_csv(f'/Users/ik/Pycharm/Mitchell/240410 Curves, Meshes/mesh_v_time{i}.csv', header=None).values
    faces = pd.read_csv(f'/Users/ik/Pycharm/Mitchell/240410 Curves, Meshes/mesh_f_time{i}.csv', header=None).values

    # Convert face indices from float to int (Python uses 0-based indexing)
    faces = np.array(faces, dtype=int) - 1  # Subtract 1 if your indices are 1-based

    # Prepare the vertices for the faces
    faces_vertices = vertices[faces]

    # Create a 3D mesh
    mesh = Poly3DCollection(faces_vertices, alpha=0.01, edgecolor='k')
    ax.add_collection3d(mesh)

    #plt.savefig(f'/Users/ik/Pycharm/Mitchell/240427 Center Lines with Mesh, Frenet-Serret Frame/center_line_mesh_fs_time{i}')
    fig.legend()
    plt.tight_layout()
    plt.show()
    plt.close(fig)
