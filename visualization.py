import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import seaborn as sns
#from mayavi import mlab

def frenet_serret_frame(r):
    L = len(r)
    d3 = np.zeros((L-1, 3))     # Tangent vector
    d1 = np.zeros((L-2, 3))     # Normal vector
    K = np.zeros(L-2)           # Curvature
    d2 = np.zeros((L-2, 3))     # Binormal vector
    tau = np.zeros(L-3)         # Torsion

    # Calculate tangent vectors
    for n in range(L-1):
        d3[n] = r[n+1] - r[n]
        d3[n] = d3[n] / np.linalg.norm(d3[n])

    # Calculate normal vectors and curvature
    for n in range(L-2):
        d1[n] = d3[n+1] - d3[n]
        K[n] = np.linalg.norm(d1[n])
        if K[n] != 0:  # Avoid division by zero
            d1[n] = d1[n] / K[n]
        d2[n] = np.cross(d3[n], d1[n])

    # Calculate torsion
    for n in range(L-3):
        tau[n] = (-1) * np.inner(d1[n], d2[n + 1] - d2[n])

    return d1, d2, d3, K, tau
# L x 3 Position arrays => Frenet-Serret frames (d1, d2, d3), Curvature (K), Torsion (tau)


def frenet_serret_frame2(r):
    L = len(r)
    d3 = np.zeros((L-1, 3))     # Tangent vector
    d1 = np.zeros((L-2, 3))     # Normal vector
    K = np.zeros(L-2)           # Curvature
    d2 = np.zeros((L-2, 3))     # Binormal vector
    tau = np.zeros(L-3)         # Torsion

    # Calculate tangent vectors
    for n in range(L-1):
        d3[n] = r[n+1] - r[n]
        d3[n] = d3[n] / np.linalg.norm(d3[n])

    # Calculate normal vectors and curvature
    for n in range(L-2):
        d2[n] = np.cross(d3[n], d3[n+1])
        d1[n] = np.cross(d2[n], d3[n])
        K[n] = np.linalg.norm(d3[n+1]-d3[n])

    # Calculate torsion
    for n in range(L-3):
        tau[n] = (-1) * np.inner(d1[n], d2[n + 1] - d2[n])

    return d1, d2, d3, K, tau
# Position arrays (r) => Frenet-Serret frames (d1, d2, d3), Curvature (K), Torsion (tau)


def frenet_serret_frame_savitzky_golay(r, w, p):
    L = len(r)
    K = np.zeros(L)
    tau = np.zeros(L-1)

    # Smooth positions by using the Savitzky-Golay filter
    r_smooth_der1 = savgol_filter(r, w, polyorder=p, axis=0, mode='nearest', deriv=1)
    norms_der1 = np.linalg.norm(r_smooth_der1, axis=1, keepdims=True)

    # Define the Frenet-Serret frame
    d3 = r_smooth_der1 / norms_der1                                             # Tangent vectors
    d1 = savgol_filter(d3, w, polyorder=p, axis=0, mode='nearest', deriv=1)     # Normal vectors
    K = np.linalg.norm(d1, axis=1, keepdims=True)                               # Curvatures
    d1 = d1 / K
    d2 = np.cross(d3, d1, axis=1)                                               # Binormal vectors

    # Calculate torsion
    for n in range(L-1):
        tau[n] = (-1) * np.inner(d1[n], d2[n + 1] - d2[n])

    return d1, d2, d3, K, tau
# Savitzky-Golay filter


def ribbon_frame(r1, r2):
    L = len(r)
    d3 = np.zeros((L-1, 3))     # Tangent vector
    d1 = np.zeros((L-2, 3))     # Normal vector
    K = np.zeros(L-2)           # Curvature
    d2 = np.zeros((L-2, 3))     # Binormal vector
    tau = np.zeros(L-3)         # Torsion

    # Calculate tangent vectors
    for n in range(L-1):
        d3[n] = r[n+1] - r[n]
        d3[n] = d3[n] / np.linalg.norm(d3[n])

    # Calculate normal vectors and curvature
    for n in range(L-2):
        d1[n] = d3[n+1] - d3[n]
        K[n] = np.linalg.norm(d1[n])
        if K[n] != 0:  # Avoid division by zero
            d1[n] = d1[n] / K[n]
        d2[n] = np.cross(d3[n], d1[n])

    # Calculate torsion
    for n in range(L-3):
        tau[n] = (-1) * np.inner(d1[n], d2[n + 1] - d2[n])

    return d1, d2, d3, K, tau
# Position arrays (r1, r2) => Ribbon frames (d1, d2, d3), Curvature (K), Torsion (tau)


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


def fourplots(r, tau, angles, cmap):
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
        sc = ax.scatter(r[1:L + 1, 0], r[1:L + 1, 1], r[1:L + 1, 2], c=tau, cmap=cmap, norm=Normalize(vmin=-1, vmax=1))
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
cmap1 = sns.diverging_palette(250, 55, l=85, s=100, center="dark", as_cmap=True)       # Blue(-) Yellow(+)

# Import data and make plots
for i in range(60, 61):
    r = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv', delimiter=',', skip_header=1)

    d1, d2, d3, K, tau = frenet_serret_frame2(r)
    #d1, d2, d3, K, tau = frenet_serret_frame_savitzky_golay(r, 5, 2)

    #fig = fourplots(r, tau, [(30, -30), (90, -90), (0, -90), (0, 180)], 'tab10')
    fig = plot(r, tau, [90, 0], cmap1)

    #fig.suptitle(f'Frenet-Serret, Time {i}', fontsize=20, fontweight='bold')
    fig.suptitle(f'Frenet-Serret, Savitzky-Golay, Time {i}', fontsize=20, fontweight='bold')
    #plt.savefig(f'centerline_fs_savgol_{i}.png')
    plt.show()
    plt.close(fig)