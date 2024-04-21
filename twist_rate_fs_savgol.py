import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab
from scipy.signal import savgol_filter

# Import coordinates of points on the center line
for i in range(1, 61):
    r = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv',
                      delimiter=',', skip_header=1)

    # Smooth positions by using the Savitzky-Golay filter
    w = 10
    p = 2
    r_smooth = savgol_filter(r, w, polyorder=p, axis=0, mode='nearest')
    r_smooth_der1 = savgol_filter(r, w, polyorder=p, axis=0, mode='nearest', deriv=1)
    norms_der1 = np.linalg.norm(r_smooth_der1, axis=1, keepdims=True)

    # Define the Frenet-Serret frame
    d3 = r_smooth_der1 / norms_der1     # Tangent vectors
    d1 = savgol_filter(d3, w, polyorder=p, axis=0, mode='nearest', deriv=1)
    d1 = d1 / np.linalg.norm(d1, axis=1, keepdims=True)
    d2 = np.cross(d3, d1, axis=1)

    # Calculate torsion
    tau = np.zeros(99)
    for n in range(99):
        tau[n] = (-1) * np.inner(d1[n], d2[n + 1] - d2[n])

    # Define angles (elevation, azimuth)
    angles = [(30, 30), (30, 120), (60, 30), (60, 120)]

    # Determine the range for all axes
    max_range = np.array([r[1:100, 0].max()-r[1:100, 0].min(),
                          r[1:100, 1].max()-r[1:100, 1].min(),
                          r[1:100, 2].max()-r[1:100, 2].min()]).max() / 2.0

    mid_x = (r[1:100, 0].max() + r[1:100, 0].min()) / 2.0
    mid_y = (r[1:100, 1].max() + r[1:100, 1].min()) / 2.0
    mid_z = (r[1:100, 2].max() + r[1:100, 2].min()) / 2.0

    # Create a figure with subplots
    fig = plt.figure(figsize=(20, 15))

    for j, angle in enumerate(angles, start=1):
        ax = fig.add_subplot(2, 2, j, projection='3d')
        sc = ax.scatter(r[1:100, 0], r[1:100, 1], r[1:100, 2], c=tau, cmap='plasma')
        ax.view_init(elev=angle[0], azim=angle[1])

        # Setting the same scale for all axes
        ax.set_xlim(mid_x - max_range, mid_x + max_range)
        ax.set_ylim(mid_y - max_range, mid_y + max_range)
        ax.set_zlim(mid_z - max_range, mid_z + max_range)

        ax.set_title(f'View {j}: Elevation={angle[0]}, Azimuth={angle[1]}')

    # Add a color bar
    fig.subplots_adjust(right=0.8)  # Adjust subplot to not overlap with colorbar
    cbar_ax = fig.add_axes([0.90, 0.15, 0.02, 0.7])  # Position of colorbar: [left, bottom, width, height]
    cbar = fig.colorbar(sc, cax=cbar_ax)
    cbar.set_label('Twist Rate', fontsize=15, rotation=270, labelpad=15)

    #plt.tight_layout()
    fig.suptitle(f'Frenet-Serret, Savitzky-Golay, Time {i}', fontsize=20, fontweight='bold')
    plt.savefig(f'centerline_fs_savgol_{i}.png', bbox_inches='tight')
    plt.close(fig)