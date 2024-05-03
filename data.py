import numpy as np

for j in range(1, 2):
    data = np.zeros((60, 99))
    for i in range(0, 60):
        data[i] = np.genfromtxt(f"/Users/ik/Pycharm/Mitchell/240502 Average Twist/average_twist_time{i+1}")

    np.savetxt(f"twist_average.csv", data, delimiter=",", header="Row: Time, Column: Sampled points")