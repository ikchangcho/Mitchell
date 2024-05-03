from frames import *
from visualization import *

data = np.genfromtxt("twist_average.csv", delimiter=",", skip_header=1)
data1 = np.genfromtxt("twist_ribbon1.csv", delimiter=",", skip_header=1)
data2 = np.genfromtxt("twist_ribbon2.csv", delimiter=",", skip_header=1)
data3 = np.genfromtxt("twist_ribbon3.csv", delimiter=",", skip_header=1)
data4 = np.genfromtxt("twist_ribbon4.csv", delimiter=",", skip_header=1)
labels = ["Ribbon1", "Ribbon2", "Ribbon3", "Ribbon4"]

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

for i in range(60):
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(data[i])

    ax.grid()
    ax.set_xlabel("Sampled Points")
    ax.set_ylabel("Twist (rad)")
    ax.set_ylim(-3, 3.5)
    ax.set_title(f"Average Twist, Time {i+1:02}")
    plt.savefig(f"/Users/ik/Pycharm/Mitchell/240502 Twist, Average/twist_average_time{i+1:02}.png")
    plt.close(fig)