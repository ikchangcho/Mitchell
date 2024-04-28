import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import colormaps as cmaps
import seaborn as sns


def trajectory(r, tau, angle, cmap):
    L = len(tau)

    fig = plt.figure(figsize=(20, 15))

    ax = fig.add_subplot(1, 1, 1, projection='3d')
    sc = ax.scatter(r[1:L + 1, 0], r[1:L + 1, 1], r[1:L + 1, 2], c=tau, cmap=cmap)
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

def four_trajectories_norm(r, tau, angles, cmap, vmin, vmax):
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
        sc = ax.scatter(r[1:L + 1, 0], r[1:L + 1, 1], r[1:L + 1, 2], c=tau, cmap=cmap, norm=Normalize(vmin=vmin, vmax=vmax))
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

j = 4   # Curve number
for i in range(1, 61):

    rc = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv', delimiter=',', skip_header=1)
    torsion = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240427 Torsion/torsion_time{i}.csv')
    twist_rate = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240427 Twist Rate, Ribbon Frame {j}/twist_rate_ribbon{j}_time{i}.csv')

    fig = four_trajectories_norm(rc, twist_rate, [(30, -30), (90, -90), (0, -90), (0, 180)], cmaps.berlin, -1.0, 1.0)
    #fig = trajectory(rc, twist_rate, [30, -30], cmaps.berlin)
    fig.suptitle(f'Ribbon Frame {j}, Time {i:02}', fontsize=20, fontweight='bold')

    # Save or show
    plt.savefig(f'/Users/ik/Pycharm/Mitchell/240427 Center Lines, Ribbon Frame {j}/centerline_ribbon{j}_time{i:02}.png')
    #plt.show()
    plt.close(fig)