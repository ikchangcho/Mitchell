from frames import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import colormaps as cmaps


j = 4
for w in range(3, 31):
    threshold = 0.3
    data_arrays = None

    for i in range(1, 61):  # Adjust range for the number of files
        rc = np.genfromtxt(f"/Users/ik/Pycharm/Mitchell/240411 Curves, Centerlines (Resampled to 100)/tp{i:06}_centerline.csv", delimiter=",", skip_header=1)
        d1, d2, d3, K, tau, Tw = frenet_serret_frame_savitzky_golay(rc, w, 2)

        if data_arrays is None:
            data_arrays = tau
        else:
            data_arrays = np.vstack([data_arrays, tau])

    over_saturated = (np.abs(np.array(data_arrays)) > threshold).sum()

    # Create a heatmap
    fig, ax = plt.subplots(figsize=(10, 5)) # You can adjust the size as needed
    sns.heatmap(data_arrays, ax=ax, annot=False, cmap="RdBu_r", xticklabels=1, yticklabels=1, vmin=-threshold, vmax=threshold)

    # # Display the count of exceeding elements on the heatmap
    # text = f"Oversaturated: {over_saturated}"
    # ax.text(100, 60, text, verticalalignment='top', horizontalalignment='right', color='black', fontsize=10)

    # Customizing x and y ticks:
    # Select specific ticks to display on x-axis, e.g., every 10th label
    x_ticks = np.arange(0, 99, 10)  # Modify step size as needed
    plt.xticks(x_ticks, [str(i+1) for i in x_ticks])  # Set x-axis tick positions and labels

    # Select specific ticks to display on y-axis, e.g., every 5th label
    y_ticks = np.arange(0, 60, 5)  # Modify step size as needed
    plt.yticks(y_ticks, [str(i+1) for i in y_ticks])  # Set y-axis tick positions and labels

    plt.xlabel('')
    plt.ylabel('Time')
    plt.title(f'Torsion, Savitky-Golay, w={w}, p=2 (Over Saturated: {over_saturated}/{60 * 99})')
    plt.savefig(f'heatmap_torsion_sg_w{w}_p2.png')
    #plt.show()
    plt.close(fig)
