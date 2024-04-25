from functions import *
import colormaps as cmaps
import seaborn as sns

# T0-Do
# Automatically adjust color bar range according to tau values
# Color bar
# Mesh trisurf


def plot(r, tau, angle, cmap):
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

    ax = fig.add_subplot(1, 1, 1, projection='3d')
    sc = ax.scatter(r[1:L + 1, 0], r[1:L + 1, 1], r[1:L + 1, 2], c=tau, cmap=cmap)
    ax.view_init(elev=angle[0], azim=angle[1])

    # Setting the same scale for all axes
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

def fourplots_norm(r, tau, angles, cmap, vmin, vmax):
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

j = 1   # Curve number
for i in range(60, 61):
    # Import file
    rc = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv', delimiter=',', skip_header=1)
    r = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240410 Curves, Meshes/curv{j}_time{i}.csv', delimiter=',', skip_header=1)

    # Define frames
    #d1, d2, d3, K, tau = ribbon_frame(rc, r)
    d10, d20, d30, K0, tau0 = frenet_serret_frame2(rc)
    #d1, d2, d3, K, tau = frenet_serret_frame_savitzky_golay(r, 5, 2)

    # Plot
    #fig = fourplots_norm(rc, tau, [(30, -30), (90, -90), (0, -90), (0, 180)], cmap1, -0.6, 0.6)
    fig = plot(rc, tau0, [30, -30], cmaps.roma)
    fig.suptitle(f'Ribbon Frame {j}, Time {i:02}', fontsize=20, fontweight='bold')

    # Save of show
    #plt.savefig(f'centerline_ribbon{j}_{i:02}.png')
    plt.savefig('roma.png')
    #plt.show()
    plt.close(fig)