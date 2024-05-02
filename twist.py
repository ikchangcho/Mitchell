from frames import *
import numpy as np
import os
import matplotlib.pyplot as plt

for i in range(1, 61):
    data = np.zeros(99)
    for j in range(1, 5):
        data += np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/250502 Twist, Ribbon {j}/twist_ribbon{j}_time{i:02}.csv', delimiter=',')
    data = data / 4
    np.savetxt(f'average_twist_time{i}', data, delimiter=",")



# data = np.genfromtxt('twist_over_time.csv', delimiter=",")
#
# fig, ax = plt.subplots()
# labels = ['Ribbon 1', 'Ribbon 2', 'Ribbon 3', 'Ribbon 4']
#
# for i in range(4):
#     ax.plot(data[i], label=labels[i])
# ax.legend(fontsize=10)
# ax.grid()
# ax.set_xlabel("Time")
# ax.set_ylabel("Twist (rad)")
# ax.set_title("Twist at the end of the curve")
# plt.savefig("Twist vs Time.png")
# plt.show()


# Twist over time
# Tw = np.zeros((4, 60))
#
# for j in range(1, 5):
#     for i in range(1, 61):
#         data = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/250502 Twist, Ribbon {j}/twist_ribbon{j}_time{i:02}.csv', delimiter=',')
#         Tw[j-1, i-1] = data[-1]
#
# np.savetxt('twist_over_time.csv', Tw, delimiter=",")

