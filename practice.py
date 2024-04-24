import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

test code

# Create sample data
c1 = np.random.randn(10, 10) * 0.5  # Smaller range of values
c2 = np.random.randn(10, 10) * 1.5  # Larger range of values

# Normalize the color scale from -1 to 1
norm = Normalize(vmin=-1, vmax=1)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# First plot
im1 = axes[0].imshow(c1, cmap='coolwarm', norm=norm)
fig.colorbar(im1, ax=axes[0], ticks=np.linspace(-1, 1, 9))
axes[0].set_title('Plot 1')

# Second plot
im2 = axes[1].imshow(c2, cmap='coolwarm', norm=norm)
fig.colorbar(im2, ax=axes[1], ticks=np.linspace(-1, 1, 9))
axes[1].set_title('Plot 2')

plt.show()
