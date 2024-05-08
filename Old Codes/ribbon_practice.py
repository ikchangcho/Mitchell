import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm
import colormaps as cmaps

# Not understanding about the color normalization

# Initialize the curves
rc = np.zeros((10, 3))
rc[:, 0] = np.arange(10)
r = rc + [0, 0, 1]

# Sample color values, one for each segment
colors = np.linspace(0, 0.1, 9)  # Just an example, replace with your actual values

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Prepare to collect triangles and their colors
triangles = []
color_map = []

# Generate triangles
for i in range(len(rc) - 1):
    # Points
    p1 = rc[i]
    p2 = rc[i + 1]
    p3 = r[i + 1]
    p4 = r[i]

    # First triangle (p1, p2, p3)
    triangles.append([p1, p2, p3])
    color_map.append(colors[i])

    # Second triangle (p1, p3, p4)
    triangles.append([p1, p3, p4])
    color_map.append(colors[i])

# Normalize color_map manually
norm = plt.Normalize(vmin=min(color_map), vmax=max(color_map))
normalized_colors = cmaps.berlin(norm(color_map))

# Create a Poly3DCollection
tri_collection = Poly3DCollection(triangles, facecolors=normalized_colors)

# Add to axis
ax.add_collection3d(tri_collection)

# Setting the limits
ax.set_xlim([0, 10])
ax.set_ylim([0, 1])
ax.set_zlim([0, 2])

# Add a color bar
sm = plt.cm.ScalarMappable(cmap=cmaps.berlin, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, pad=0.1)

# Show plot
plt.show()
plt.close(fig)
