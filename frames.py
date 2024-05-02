import numpy as np
from scipy.signal import savgol_filter

# To-Do
# frenet_serret_frame(), frenet_serret_frame_savitzky_golay(): Curvature

def frenet_serret_frame(r):
    L = len(r)
    d3 = np.zeros((L-1, 3))     # Tangent vector
    d1 = np.zeros((L-2, 3))     # Normal vector
    K = np.zeros(L-2)           # Curvature
    d2 = np.zeros((L-2, 3))     # Binormal vector
    tau = np.zeros(L-3)         # Torsion
    Tw = np.zeros(L-2)          # Twist

    # Calculate tangent vectors
    for n in range(L-1):
        d3[n] = r[n+1] - r[n]
        d3[n] = d3[n] / np.linalg.norm(d3[n])

    # Calculate normal vectors and curvature
    for n in range(L-2):
        d1[n] = (d3[n+1] - d3[n]) / np.linalg.norm(r[n+1] - r[n])
        K[n] = np.linalg.norm(d1[n])
        if K[n] != 0:  # Avoid division by zero
            d1[n] = d1[n-1]
        else:
            d1[n] = d1[n] / K[n]
        d2[n] = np.cross(d3[n], d1[n])

    # Calculate torsion
    for n in range(L-3):
        tau[n] = (-1) * np.inner(d1[n], (d2[n + 1] - d2[n]) / np.linalg.norm(r[n+1] - r[n]))
        Tw[n+1] = Tw[n] - np.inner(d1[n], (d2[n + 1] - d2[n]))

    return d1, d2, d3, K, tau, Tw
# L x 3 Position array => Frenet-Serret frames (d1, d2, d3), Curvature (K), Torsion (tau)


def frenet_serret_frame_savitzky_golay(r, w, p):
    L = len(r)
    K = np.zeros(L)
    tau = np.zeros(L-1)
    Tw = np.zeros(L)

    # Smooth positions by using the Savitzky-Golay filter
    r_smooth_der1 = savgol_filter(r, w, polyorder=p, axis=0, mode='mirror', deriv=1)
    norms_der1 = np.linalg.norm(r_smooth_der1, axis=1, keepdims=True)

    # Define the Frenet-Serret frame
    d3 = r_smooth_der1 / norms_der1                                             # Tangent vectors
    d1 = savgol_filter(d3, w, polyorder=p, axis=0, mode='nearest', deriv=1)     # Normal vectors
    K = np.linalg.norm(d1, axis=1, keepdims=True)                               # Curvatures
    d1 = d1 / K
    d2 = np.cross(d3, d1, axis=1)                                               # Binormal vectors

    # Calculate torsion
    for n in range(L-1):
        tau[n] = (-1) * np.inner(d1[n], (d2[n + 1] - d2[n]) / np.linalg.norm(r[n+1] - r[n]))
        Tw[n + 1] = Tw[n] - np.inner(d1[n], (d2[n + 1] - d2[n]))

    return d1, d2, d3, K, tau, Tw
# Savitzky-Golay filter
# Curvature is not reliable!


def frenet_serret_frame2(r):
    L = len(r)
    d3 = np.zeros((L-1, 3))     # Tangent vector
    d1 = np.zeros((L-2, 3))     # Normal vector
    K = np.zeros(L-2)           # Curvature
    d2 = np.zeros((L-2, 3))     # Binormal vector
    tau = np.zeros(L-3)         # Torsion
    Tw = np.zeros(L-2)

    # Calculate tangent vectors
    for n in range(L-1):
        d3[n] = r[n+1] - r[n]
        d3[n] = d3[n] / np.linalg.norm(d3[n])

    # Calculate normal vectors
    for n in range(L-2):
        d2[n] = np.cross(d3[n], d3[n+1])
        if np.linalg.norm(d2[n]) == 0:
            d2[n] = d2[n-1]
        else:
            d2[n] = d2[n] / np.linalg.norm(d2[n])
        d1[n] = np.cross(d2[n], d3[n])

    # Calculate torsion
    for n in range(L-3):
        tau[n] = (-1) * np.inner(d1[n], (d2[n + 1] - d2[n]) / np.linalg.norm(r[n+1] - r[n]))
        Tw[n + 1] = Tw[n] - np.inner(d1[n], (d2[n + 1] - d2[n]))

    return d1, d2, d3, K, tau, Tw
# Position arrays (r) => Frenet-Serret frames (d1, d2, d3), Curvature (K), Torsion (tau)
# Curvature is not reliable

def ribbon_frame(center, edge):
    L = len(center)
    d3 = np.zeros((L-1, 3))     # Tangent vector
    d1 = np.zeros((L-1, 3))     # Normal vector
    K = np.zeros(L-1)           # Curvature
    d2 = np.zeros((L-1, 3))     # Binormal vector
    tau = np.zeros(L-2)         # Torsion
    Tw = np.zeros(L-1)          # Twist

    # Calculate tangent vectors
    for n in range(len(d3)):
        d3[n] = center[n+1] - center[n]
        d3[n] = d3[n] / np.linalg.norm(d3[n])

    # Calculate normal vectors and curvature
    for n in range(len(d1)):
        d1[n] = (edge[n] - center[n]) - np.inner(edge[n] - center[n], d3[n]) * d3[n]
        if np.linalg.norm(d1[n]) == 0:
            d1[n] = d1[n-1]
        else:
            d1[n] = d1[n] / np.linalg.norm(d1[n])

        d2[n] = np.cross(d3[n], d1[n])

    # Calculate torsion
    for n in range(len(tau)):
        tau[n] = (-1) * np.inner(d1[n], d2[n + 1] - d2[n])
        Tw[n + 1] = Tw[n] - np.inner(d1[n], (d2[n + 1] - d2[n]))

    return d1, d2, d3, K, tau, Tw
# Position arrays (r1, r2) => Ribbon frames (d1, d2, d3), Curvature (K), Torsion (tau)



w = 5
for j in range(1, 5):
    for i in range(1, 61):
        rc = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv', delimiter=',', skip_header=1)
        r = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_curv{j}.csv', delimiter=',', skip_header=1)

        d1, d2, d3, K, tau, Tw = ribbon_frame(rc, r)

        np.savetxt(f'/Users/ik/Pycharm/Mitchell/250502 Twist, Ribbon {j}/twist_ribbon{j}_time{i:02}.csv', Tw, delimiter=",")


#tau_range = np.zeros((5, 2))

# # Find the range of the torsion
# min_max_torsion = np.zeros((60, 2))
# for i in range(1, 61):
#     torsion = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240427 Torsion/torsion_time{i}.csv')
#     min_max_torsion[i - 1] = [np.min(torsion), np.max(torsion)]
#
# tau_range[0, 0], tau_range[0, 1] = np.min(min_max_torsion[:, 0]), np.max(min_max_torsion[:, 1])

# # Find the range of the twist rate
# for j in range(1, 5):
#     min_max_twist_rate = np.zeros((60, 2))
#     for i in range(1, 61):
#         twist_rate = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240427 Twist Rate, Ribbon Frame {j}/twist_rate_ribbon{j}_time{i}.csv')
#         min_max_twist_rate[i - 1] = [np.min(twist_rate), np.max(twist_rate)]
#
#     tau_range[j, 0], tau_range[j, 1] = np.min(min_max_twist_rate[:, 0]), np.max(min_max_twist_rate[:, 1])
#
# np.savetxt(f'/Users/ik/Pycharm/Mitchell/twist_rate_range.csv', tau_range, delimiter=',', fmt='%.2f')