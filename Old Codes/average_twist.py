import numpy as np


data1 = np.genfromtxt("../CSV/twist_rate_ribbon1.csv", delimiter=",", skip_header=1)
data2 = np.genfromtxt("../CSV/twist_rate_ribbon2.csv", delimiter=",", skip_header=1)
data3 = np.genfromtxt("../CSV/twist_rate_ribbon3.csv", delimiter=",", skip_header=1)
data4 = np.genfromtxt("../CSV/twist_rate_ribbon4.csv", delimiter=",", skip_header=1)
data = np.genfromtxt("../CSV/torsion.csv", delimiter=",", skip_header=1)
np.savetxt("../CSV/twist_rate_average.csv", data, delimiter=",", header="Row: Time, Column: Sampled points")



for i in range(1, 61):
    data = np.zeros(99)
    for j in range(1, 5):
        data += np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/250502 Twist, Ribbon {j}/twist_ribbon{j}_time{i:02}.csv', delimiter=',')
    data = data / 4
    np.savetxt(f'average_twist_time{i}', data, delimiter=",")



