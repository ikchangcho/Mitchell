import numpy as np

distance = np.zeros((60, 99))
for j in range(60):
    data = np.genfromtxt(f"/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{j+1:06}_centerline.csv", delimiter=",", skip_header=1)
    for i in range(99):
        distance[j, i] = np.linalg.norm(data[i] - data[i+1])

#np.savetxt("../distance_between_points.csv", distance, delimiter=",", header="Row: Time, Column: 1~2, 2~3, ... , 99~100")

accum_distance = np.cumsum(distance, axis=1)
accum_distance = np.hstack((np.zeros((accum_distance.shape[0], 1)), accum_distance))
np.savetxt("../accumulative_distance.csv", accum_distance, delimiter=",", header="Row: Time, Column: 1~2, 2~3, ... , 99~100")