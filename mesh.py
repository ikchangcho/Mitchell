import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Load data
vertices = pd.read_csv('/Users/ik/Pycharm/Mitchell/Old Data/240410 Curves, Meshes/mesh_v_time1.csv', header=None).values
faces = pd.read_csv('/Users/ik/Pycharm/Mitchell/Old Data/240410 Curves, Meshes/mesh_f_time1.csv', header=None).values

# Convert face indices from float to int (Python uses 0-based indexing)
faces = np.array(faces, dtype=int) - 1  # Subtract 1 if your indices are 1-based

# Prepare the vertices for the faces
faces_vertices = vertices[faces]

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a 3D mesh
mesh = Poly3DCollection(faces_vertices, alpha=0.01, edgecolor='k')
ax.add_collection3d(mesh)

# Scale the axes equally (important for a correct spatial representation)
max_range = np.array([vertices[:, 0].max()-vertices[:, 0].min(),
                      vertices[:, 1].max()-vertices[:, 1].min(),
                      vertices[:, 2].max()-vertices[:, 2].min()]).max() / 2.0

mid_x = (vertices[:, 0].max() + vertices[:, 0].min()) * 0.5
mid_y = (vertices[:, 1].max() + vertices[:, 1].min()) * 0.5
mid_z = (vertices[:, 2].max() + vertices[:, 2].min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

# Show the plot
plt.show()