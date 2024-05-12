import numpy as np
from frames import *
from visualization import *

data1 = np.genfromtxt("twist_ribbon1.csv", delimiter=",", skip_header=1)
data2 = np.genfromtxt("twist_ribbon2.csv", delimiter=",", skip_header=1)
data3 = np.genfromtxt("twist_ribbon3.csv", delimiter=",", skip_header=1)
data4 = np.genfromtxt("twist_ribbon4.csv", delimiter=",", skip_header=1)
labels = ['Right Dorsal', 'Right Ventral', 'Left Ventral', 'Left Dorsal']

left = (data3 + data4) / 2
right = (data1 + data2) / 2
dorsal = (data1 + data4) / 2
ventral = (data2 + data3) / 2

accum_distance = np.genfromtxt("accumulative_distance.csv", delimiter=",", skip_header=1)

constrictions = np.genfromtxt("constrictions.csv", delimiter=",", skip_header=1)
constrictions[constrictions == 0] = np.nan

plt.close('all')
for i in range(60):
    x = accum_distance[i, :] / np.max(accum_distance[i, :])
    [c1, c2, c3] = constrictions[i]
    fig, ax = plt.subplots(figsize=(7, 5))
    # ax.plot(x[:data1.shape[1]], data1[i], label=labels[0])
    # ax.plot(x[:data2.shape[1]], data2[i], label=labels[1])
    # ax.plot(x[:data3.shape[1]], data3[i], label=labels[2])
    # ax.plot(x[:data4.shape[1]], data4[i], label=labels[3])
    ax.plot(x[:left.shape[1]], dorsal[i], label='Dorsal')
    ax.plot(x[:right.shape[1]], ventral[i], label='Ventral')
    ax.axvline(x=c1, color='red', linestyle='--', linewidth=1)
    ax.axvline(x=c2, color='red', linestyle='--', linewidth=1)
    ax.axvline(x=c3, color='red', linestyle='--', linewidth=1)

    ax.grid()
    ax.set_xlabel("s/L")
    ax.set_ylabel("Twist (rad)")
    ax.set_ylim(-3, 5)
    ax.set_title(f"Averaged Twist on the Dorsal and Ventral")
    ax.legend(loc="upper left", fontsize="small")
    ax.text(1.04, 5.1, f'{i*2} min', fontsize=10, ha="right")

    #plt.show()
    plt.savefig(f"/Users/ik/Pycharm/Mitchell/twist_dorsal_ventral_time{i+1:02}.png")
    plt.close(fig)

# plt.close('all')
# for w in range(1):
#     data = np.genfromtxt(f"torsion.csv", delimiter=",", skip_header=1)
#     data2 = np.genfromtxt(f"Torsion2.csv", delimiter=",", skip_header=1)
#     for i in range(60, 61):
#         fig, ax = plt.subplots(figsize=(7, 5))
#         ax.plot(accum_distance[i-1,:len(data[i-1])], data[i-1])
#         ax.plot(accum_distance[i-1,:len(data2[i-1])], data2[i-1])
#
#         ax.grid()
#         ax.set_xlabel(r"Curve Length ($\mu m$)")
#         ax.set_ylabel(r"Torsion (rad/$\mu m$)")
#         ax.set_ylim()
#         ax.set_title(f"Torsion, Time {i:02}")
#         #plt.savefig(f"/Users/ik/Pycharm/Mitchell/240508 Twist Plots, Frenet-Serret Frame, Savistzky-Golay, w={w}/twist_fr_sg_w{w}_p2_time{i:02}.png")
#         plt.show()