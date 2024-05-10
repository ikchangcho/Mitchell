from frames import *

torsion = np.zeros((60, 97))

for tp in range(1, 61):
    r = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{tp:06}_centerline.csv', delimiter=',', skip_header=1)
    d1, d2, d3, K, tau, Tw = frenet_serret_frame2(r)
    torsion[tp-1] = tau

np.savetxt(f"Torsion2.csv", torsion, delimiter=",", header="Row: Time, Column: Sample Points")