import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

tp = 1
data = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{tp:06}_centerline.csv', delimiter=",", skip_header=1)
tangents = np.zeros((99, 3))

for i in range(99):
    tangents[i] = data[i+1] - data[i]
    tangents[i] = tangents[i] / np.linalg.norm(tangents[i])

for i in range(98, 99):

    # Create a sphere
    phi, theta = np.mgrid[0.0:2*np.pi:100j, 0.0:np.pi:50j]
    x = np.sin(theta)*np.cos(phi)
    y = np.sin(theta)*np.sin(phi)
    z = np.cos(theta)

    # Set up the figure and 3D axis
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the sphere
    ax.plot_surface(x, y, z, color='white', alpha=0.2, linewidth=0)  # semi-transparent sphere

    # Plot the vector and Trajectory
    ax.plot(tangents[:i+1, 0], tangents[:i+1, 1], tangents[:i+1:, 2], color='r', linestyle='-', marker='o')
    ax.quiver(0, 0, 0, tangents[i, 0], tangents[i, 1], tangents[i, 2], color='r')

    # Set limits and labels
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Aspect ratio to 1 to ensure the sphere isn't distorted
    ax.set_box_aspect([1,1,1])  # Equal aspect ratio
    ax.grid(False)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([-1, 0, 1])
    ax.view_init(elev=0, azim=90)
    ax.set_title(f"Tangent Vector at the {i+1}th Point")

    plt.suptitle(f"Time {tp:02}")
    plt.savefig(f'/Users/ik/Pycharm/Mitchell/240508 Tangent Vectors Trajectory, Time 01/tagent_vectors_point_{i+1:02}_time{tp:02}.png')
    plt.show()
    plt.close(fig)



