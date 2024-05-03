from frames import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import colormaps as cmaps
import seaborn as sns


def trajectory(r, tau, angle, cmap, threshold):
    L = len(tau)

    fig = plt.figure(figsize=(20, 15))

    ax = fig.add_subplot(1, 1, 1, projection='3d')
    sc = ax.scatter(r[1:L + 1, 0], r[1:L + 1, 1], r[1:L + 1, 2], c=tau, cmap=cmap, norm=Normalize(vmin=-threshold, vmax=threshold))
    ax.view_init(elev=angle[0], azim=angle[1])

    # Setting the same scale for all axes
    max_range = 140
    mid_x = (250 + -50) / 2.0
    mid_y = (100 + -100) / 2.0
    mid_z = (100 + -100) / 2.0
    # max_range = np.array([r[1:L+1, 0].max() - r[1:L+1, 0].min(),
    #                       r[1:L+1, 1].max() - r[1:L+1, 1].min(),
    #                       r[1:L+1, 2].max() - r[1:L+1, 2].min()]).max() / 2.0
    #
    # mid_x = (r[1:L+1, 0].max() + r[1:L+1, 0].min()) / 2.0
    # mid_y = (r[1:L+1, 1].max() + r[1:L+1, 1].min()) / 2.0
    # mid_z = (r[1:L+1, 2].max() + r[1:L+1, 2].min()) / 2.0

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # Add a color bar
    fig.subplots_adjust(right=0.8)  # Adjust subplot to not overlap with colorbar
    cbar_ax = fig.add_axes([0.90, 0.15, 0.02, 0.7])  # Position of colorbar: [left, bottom, width, height]
    cbar = fig.colorbar(sc, cax=cbar_ax)
    cbar.set_label('Twist Rate', fontsize=15, rotation=270, labelpad=15)

    return fig
# => Figure
# Create a 3D trajectory

def four_trajectories(r, tau, angles, cmap, threshold):
    L = len(tau)
    max_range = 140
    mid_x = (250 + -50) / 2.0
    mid_y = (100 + -100) / 2.0
    mid_z = (100 + -100) / 2.0
    # max_range = np.array([r[1:L+1, 0].max() - r[1:L+1, 0].min(),
    #                       r[1:L+1, 1].max() - r[1:L+1, 1].min(),
    #                       r[1:L+1, 2].max() - r[1:L+1, 2].min()]).max() / 2.0
    #
    # mid_x = (r[1:L+1, 0].max() + r[1:L+1, 0].min()) / 2.0
    # mid_y = (r[1:L+1, 1].max() + r[1:L+1, 1].min()) / 2.0
    # mid_z = (r[1:L+1, 2].max() + r[1:L+1, 2].min()) / 2.0

    fig = plt.figure(figsize=(20, 15))

    for j, angle in enumerate(angles, start=1):
        ax = fig.add_subplot(2, 2, j, projection='3d')
        sc = ax.scatter(r[1:L + 1, 0], r[1:L + 1, 1], r[1:L + 1, 2], c=tau, cmap=cmap, norm=Normalize(vmin=-threshold, vmax=threshold))
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

    return fig
# => Figure
# Create four subplots of the trajectory from different angles


# Customized color maps
cmap1 = sns.diverging_palette(260, 100, l=85, s=100, center="dark", as_cmap=True)


# # Make plots
# cmap = cmaps.berlin
# threshold = 0.1
# init_time = 1
# final_time = 61
#
# j = 4   # Curve number
# for w in range(30, 31):
#     print(f'PROGRESS: w={w}')
#     for i in range(init_time, final_time):
#
#         rc = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv', delimiter=',', skip_header=1)
#         #tau = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240501 Tosrion, Savitky-Golay, w=20, p=2/torsion_time{i}.csv')
#         d1, d2, d3, K, tau = frenet_serret_frame_savitzky_golay(rc, w, 2)
#
#         over_saturated = (np.abs(tau) > threshold).sum()
#         #fig = four_trajectories(rc, tau, [(30, -30), (90, -90), (0, -90), (0, 180)], cmap, threshold)
#         fig = trajectory(rc, tau, [30, -30], cmap, threshold)
#         fig.text(0.5, 0.94, f'Torsion, Savitzky-Golay, w={w}, p=2, Time {i:02}', fontsize=20, ha='center', weight='bold')
#         fig.text(0.5, 0.90, f'Oversaturated: {over_saturated}/{len(tau)}', fontsize=15, ha='center', style='italic')
#
#         # Save or show
#         plt.savefig(f'/Users/ik/Pycharm/Mitchell/240502 Centerlines, Frenet-Serret Frame, Savitsky-Golay, w={w}, p=2/centerline_time{i:02}.png')
#         #plt.show()
#         plt.close(fig)
