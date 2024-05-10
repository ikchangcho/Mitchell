import numpy as np

for w in range(3, 31):
    data = np.zeros((60, 100))
    for i in range(1, 61):
        data[i-1] = np.genfromtxt(f"/Users/ik/Pycharm/Mitchell/Torsion/twist_fr_w{w}_p2_time{i:02}.csv")

    np.savetxt(f"/Users/ik/Pycharm/Mitchell/240508 Twist, Frenet-Serret Frame, Savistzky-Golay/twist_fr_sg_w{w}_p2.csv", data, delimiter=",", header="Row: Time, Column: Sampled points")