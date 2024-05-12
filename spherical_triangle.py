import numpy as np

def cartesian_to_spherical(x):
    r = np.linalg.norm(x)
    theta = np.arctan2(np.sqrt(x[0]**2 + x[1]**2), x[2])
    phi = np.arctan2(x[1], x[0])

    return r, theta, phi

def phi_prime(theta1, phi1, theta2, phi2):
    return np.arctan2(np.sin(theta1 - theta2) * np.cos(phi1), np.sin(phi1) * np.cos(phi2) - np.cos(phi1) * np.sin(phi2) * np.cos(theta1 - theta2))
# Transform two points on the unit sphere so that theta2 becomes pi/2

def spherical_angle(A, P, B):
    if np.abs(np.linalg.norm(A) - 1) > 1e-6 or np.abs(np.linalg.norm(P) - 1) > 1e-6 or np.abs(np.linalg.norm(B) - 1) > 1e-6:
        print("The vectors are not unit vectors")

    r_A, theta_A, phi_A = cartesian_to_spherical(A)
    r_P, theta_P, phi_P = cartesian_to_spherical(P)
    r_B, theta_B, phi_B = cartesian_to_spherical(B)

    phi_A_prime = phi_prime(theta_A, phi_A, theta_P, phi_P)
    phi_B_prime = phi_prime(theta_B, phi_B, theta_P, phi_P)

    if np.abs(phi_B_prime - phi_A_prime) < np.pi:
        spherical_angle = np.abs(phi_B_prime - phi_A_prime)
    else:
        spherical_angle = 2*np.pi - np.abs(phi_B_prime - phi_A_prime)

    return spherical_angle
# Spherical angles between two great circles on the unit sphere

def spherical_area(A, B, C):
    return spherical_angle(A, B, C) + spherical_angle(B, C, A) + spherical_angle(C, A, B) - np.pi

def sign_of_area(A, B, C):
    if np.dot(A, np.cross(B-A, C-A)) >= 0:
        return 1
    else:
        return -1

# A = [1, 0, 0]
# A = A / np.linalg.norm(A)
# B = [1, 0, 0]
# B = B / np.linalg.norm(B)
# C = [0, 0, 1]
# C = C / np.linalg.norm(C)
#
# print(spherical_angle(A, B, C))
# print(spherical_angle(B, C, A))
# print(spherical_angle(C, A, B))
# print(spherical_area(A, B, C))


