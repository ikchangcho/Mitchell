from frames import *
import numpy as np

for w in range(3, 31):
    for i in range(1, 61):
        rc = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv', delimiter=',', skip_header=1)
        #r = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_curv{j}.csv', delimiter=',', skip_header=1)

        d1, d2, d3, K, tau, Tw = frenet_serret_frame_savitzky_golay(rc, w, 2)

        np.savetxt(f'/Users/ik/Pycharm/Mitchell/Torsion/twist_fr_w{w}_p2_time{i:02}.csv', Tw, delimiter=",")
