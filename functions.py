import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import seaborn as sns
#from mayavi import mlab

# To-Do
# frenet_serret_frame(), frenet_serret_frame_savitzky_golay(): Curvature

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

    return d1, d2, d3, K, tau
# L x 3 Position array => Frenet-Serret frames (d1, d2, d3), Curvature (K), Torsion (tau)


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
        tau[n] = (-1) * np.inner(d1[n], (d2[n + 1] - d2[n]) / np.linalg.norm(r[n+1] - r[n]))

    return d1, d2, d3, K, tau
# Savitzky-Golay filter
# Curvature is not reliable!


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

    # Calculate normal vectors
    for n in range(L-2):
        d2[n] = np.cross(d3[n], d3[n+1])
        if np.linalg.norm(d2[n]) != 0:
            d2[n] = d2[n] / np.linalg.norm(d2[n])
        d1[n] = np.cross(d2[n], d3[n])

    # Calculate torsion
    for n in range(L-3):
        tau[n] = (-1) * np.inner(d1[n], (d2[n + 1] - d2[n]) / np.linalg.norm(r[n+1] - r[n]))

    return d1, d2, d3, K, tau
# Position arrays (r) => Frenet-Serret frames (d1, d2, d3), Curvature (K), Torsion (tau)
# Curvature is not reliable

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

