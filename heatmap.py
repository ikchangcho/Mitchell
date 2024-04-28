import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import colormaps as cmaps

# List to store each array
data_arrays = []
j = 1

# Loop to read each CSV file
for i in range(1, 61):  # Adjust range for the number of files
    file_path = f'/Users/ik/Pycharm/Mitchell/240427 Torsion/torsion_time{i}.csv'
    df = pd.read_csv(file_path, header=None)  # Use header=None if no header row exists
    data_arrays.append(df.values.flatten())  # Convert DataFrame to 1D array

# Create a heatmap
plt.figure(figsize=(10, 5))  # You can adjust the size as needed
sns.heatmap(data_arrays, annot=False, cmap="RdBu_r", xticklabels=1, yticklabels=1)

# Customizing x and y ticks:
# Select specific ticks to display on x-axis, e.g., every 10th label
x_ticks = np.arange(0, 97, 10)  # Modify step size as needed
plt.xticks(x_ticks, [str(i+1) for i in x_ticks])  # Set x-axis tick positions and labels

# Select specific ticks to display on y-axis, e.g., every 5th label
y_ticks = np.arange(0, 60, 5)  # Modify step size as needed
plt.yticks(y_ticks, [str(i+1) for i in y_ticks])  # Set y-axis tick positions and labels

plt.xlabel('')
plt.ylabel('Time')
plt.title(f'Torsion')
plt.savefig(f'torion.png')
plt.show()
