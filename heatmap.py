from frames import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import colormaps as cmaps

constrictions = np.genfromtxt("constrictions.csv", delimiter=",", skip_header=1)
constrictions[constrictions == 0] = np.nan
constrictions = constrictions * 97

threshold = 0.3

for j in range(1, 2):
    data_arrays = None
    twist_rate = np.genfromtxt(f"twist_rate_average.csv", delimiter=",", skip_header=1)

# for w in range(20, 21):
#     data_arrays = None

    for i in range(1, 61):  # Adjust range for the number of files
        # rc = np.genfromtxt(f"/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv", delimiter=",", skip_header=1)
        # d1, d2, d3, K, tau, Tw = frenet_serret_frame_savitzky_golay(rc, w, 2)
        tau = twist_rate[i-1]

        if data_arrays is None:
            data_arrays = tau
        else:
            data_arrays = np.vstack([data_arrays, tau])

    over_saturated = (np.abs(np.array(data_arrays)) > threshold).sum()

    # Create a heatmap
    fig, ax = plt.subplots(figsize=(10, 5)) # You can adjust the size as needed
    sns.heatmap(data_arrays, ax=ax, annot=False, cmap="RdBu_r", xticklabels=1, yticklabels=1, vmin=-threshold, vmax=threshold,
                cbar_kws={"label": r"Twist Rate (rad/$\mu m$"})
    ax.plot(constrictions[:, 0], np.arange(1, 61), color="k", linewidth=1)
    ax.plot(constrictions[:, 1], np.arange(1, 61), color="k", linewidth=1)
    ax.plot(constrictions[:, 2], np.arange(1, 61), color="k", linewidth=1)

    # # Display the count of exceeding elements on the heatmap
    # text = f"Oversaturated: {over_saturated}"
    # ax.text(100, 60, text, verticalalignment='top', horizontalalignment='right', color='black', fontsize=10)

    # Customizing x and y ticks:
    x_ticks = np.arange(0, 99, 10)  # Modify step size as needed
    plt.xticks(x_ticks, [str(i) for i in x_ticks])  # Set x-axis tick positions and labels
    y_ticks = np.arange(0, 61, 5)  # Modify step size as needed
    plt.yticks(y_ticks, [2 * i for i in y_ticks])  # Set y-axis tick positions and labels

    plt.xlabel('Sampled Points')
    plt.ylabel('Time (min)')
    plt.title(f'Average Twist Rate (Over Saturated: {over_saturated}/{60 * 99})', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f'Twist Rates on the Ribbon Frames (Average).png')
    plt.show()
    plt.close(fig)
