import numpy as np
from scipy.signal import savgol_filter

def frenet_serret_frame(r):
    """Build the Frenet-Serret frame.

    Parameters
    ----------
    r : L x 3 float
        Coordinates of each point in the curve

    Returns
    -------
    d1 : (L-2) x 3 float
        Normal vectors
    d2 : (L-2) x 3 float
        Binormal vectors
    d3 : (L-1) x 3 float
        Tangent vectors
    K : (L-2) x 1 float
        Curvature
    tau : (L-3) x 1 float
        Twist rate (Torsion)
    Tw : (L-2) x 1 float
        Twist
    """

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



def frenet_serret_frame_savitzky_golay(r, w, p):
    """Build the Frenet-Serret frame from the smoothed curve by using the Savitzky-Golay filter.

    Parameters
    ----------
    r : L x 3 float
        Coordinates of each point in the curve
    w : int
        Width of the Savitzky-Golay filter
    p : int
        Degree of the polynomial of the Savitzky-Golay filter

    Returns
    -------
    d1 : L x 3 float
        Normal vectors
    d2 : L x 3 float
        Binormal vectors
    d3 : L x 3 float
        Tangent vectors
    K : L x 1 float
        Curvature (Not reliable)
    tau : (L-1) x 1 float
        Twist rate (Torsion)
    Tw : L x 1 float
        Twist
    """
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


def frenet_serret_frame2(r):
    """Build the Frenet-Serret frame by defining the binormal vectors as cross product of the tangent vectors.

    Parameters
    ----------
    r : L x 3 float
        Coordinates of each point in the curve

    Returns
    -------
    d1 : (L-2) x 3 float
        Normal vectors
    d2 : (L-2) x 3 float
        Binormal vectors
    d3 : (L-1) x 3 float
        Tangent vectors
    K : (L-2) x 1 float
        Curvature (Not reliable)
    tau : (L-3) x 1 float
        Twist rate (Torsion)
    Tw : (L-2) x 1 float
        Twist
    """
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


def ribbon_frame(center, edge):
    """Build the Ribbon frame from two curves, by defining the binormal vectors as the difference between the two curves.

    Parameters
    ----------
    center : L x 3 float
        Coordinates of each point in the center curve
    edge : L x 3 float
        Coordinates of each point in the edge curve

    Returns
    -------
    d1 : (L-1) x 3 float
        Normal vectors
    d2 : (L-1) x 3 float
        Binormal vectors
    d3 : (L-1) x 3 float
        Tangent vectors
    K : (L-1) x 1 float
        Curvature (Not reliable)
    tau : (L-2) x 1 float
        Twist rate (Torsion)
    Tw : (L-1) x 1 float
        Twist
    """
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