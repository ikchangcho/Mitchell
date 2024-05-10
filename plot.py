import numpy as np

from frames import *
from visualization import *

# data1 = np.genfromtxt("twist_ribbon1.csv", delimiter=",", skip_header=1)
# data2 = np.genfromtxt("twist_ribbon2.csv", delimiter=",", skip_header=1)
# data3 = np.genfromtxt("twist_ribbon3.csv", delimiter=",", skip_header=1)
# data4 = np.genfromtxt("twist_ribbon4.csv", delimiter=",", skip_header=1)
# labels = ["Ribbon1", "Ribbon2", "Ribbon3", "Ribbon4"]

# for i in range(60):
#     fig, ax = plt.subplots(figsize=(7, 5))
#     ax.plot(data1[i], label=labels[0])
#     ax.plot(data2[i], label=labels[1])
#     ax.plot(data3[i], label=labels[2])
#     ax.plot(data4[i], label=labels[3])
#
#     ax.grid()
#     ax.set_xlabel("Sampled Points")
#     ax.set_ylabel("Twist (rad)")
#     ax.set_ylim(-3, 5)
#     ax.set_title(f"Twist, Time {i+1:02}")
#     ax.legend()
#     #plt.show()
#     plt.savefig(f"/Users/ik/Pycharm/Mitchell/240502 Twist, Four Ribbons/twist_four_ribbons_time{i+1:02}.png")
#     plt.close(fig)

distance = np.genfromtxt("distance_between_points.csv", delimiter=",", skip_header=1)
accum_distance = np.cumsum(distance, axis=1)
accum_distance = np.hstack((np.zeros((accum_distance.shape[0], 1)), accum_distance))

for w in range(5, 31, 5):
    data = np.genfromtxt(f"240508 Twist Values, Frenet-Serret Frame, Savistzky-Golay/twist_fr_sg_w{w}_p2.csv",
                         delimiter=",", skip_header=1)
    for i in range(1, 61):
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.plot(accum_distance[i-1], data[i-1])

        ax.grid()
        ax.set_xlabel(r"Curve Length ($\mu m$)")
        ax.set_ylabel("Twist (rad)")
        ax.set_ylim(-7, 7)
        ax.set_title(f"Frenet-Serret Frame, Savitzky-Golay, w={w}, p=2, Time {i:02}")
        plt.savefig(f"/Users/ik/Pycharm/Mitchell/240508 Twist Plots, Frenet-Serret Frame, Savistzky-Golay, w={w}/twist_fr_sg_w{w}_p2_time{i:02}.png")
        #plt.show()
        plt.close(fig)