from frames import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import colormaps as cmaps

constrictions = np.genfromtxt("constrictions.csv", delimiter=",", skip_header=1)
constrictions[constrictions == 0] = np.nan
constrictions = constrictions * 99
threshold = 0.3

plt.close('all')
fig = plt.figure(figsize=(18, 10))

for j in range(1, 5):
    ax = fig.add_subplot(2, 2, j)
    twist_rates = np.genfromtxt(f"twist_rate_ribbon{j}.csv", delimiter=",", skip_header=1)
    data_arrays = None

    for i in range(60):
        tau = twist_rates[i]

        if data_arrays is None:
            data_arrays = tau
        else:
            data_arrays = np.vstack([data_arrays, tau])

    over_saturated = (np.abs(np.array(data_arrays)) > threshold).sum()

    # Create a heatmap
    sns.heatmap(data_arrays, ax=ax, annot=False, cmap="RdBu_r", xticklabels=1, yticklabels=1, vmin=-threshold,
                vmax=threshold, cbar=False)
    ax.plot(constrictions[:, 0], np.arange(1, 61), color="k", linewidth=1)
    ax.plot(constrictions[:, 1], np.arange(1, 61), color="k", linewidth=1)
    ax.plot(constrictions[:, 2], np.arange(1, 61), color="k", linewidth=1)

    # # Display the count of exceeding elements on the heatmap
    # text = f"Oversaturated: {over_saturated}"
    # ax.text(100, 60, text, verticalalignment='top', horizontalalignment='right', color='black', fontsize=10)

    # Customizing x and y ticks:
    x_ticks = np.arange(0, 99, 10)  # Modify step size as needed
    plt.xticks(x_ticks, [str(i+1) for i in x_ticks])  # Set x-axis tick positions and labels
    y_ticks = np.arange(0, 61, 5)  # Modify step size as needed
    plt.yticks(y_ticks, [2 * i for i in y_ticks])  # Set y-axis tick positions and labels

    plt.title(f'Ribbon {j} (Over Saturated: {over_saturated}/{60 * 99})')
    #plt.savefig(f'heatmap_torsion_sg_w{w}_p2.png')

# Create one common colorbar for all heatmaps
cbar_ax = fig.add_axes([0.91, 0.10, 0.02, 0.8])  # Adjust these values to fit your layout
cbar = fig.colorbar(ax.get_children()[0], cax=cbar_ax)
cbar.set_label(r'Twist Rate (rad/$\mu m$)', fontsize=15)

fig.suptitle(r"Twist Rates on the Ribbon Frames", fontsize=20, fontweight='bold')
fig.supxlabel("Sampled Points", fontsize=15)
fig.supylabel("Time (min)", fontsize=15)
plt.tight_layout(rect=[0.02, 0, 0.9, 1])
plt.savefig('Twist Rates on the Ribbon Frames.png')
