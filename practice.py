import numpy as np

data = np.genfromtxt('twist_ribbon1.csv', delimiter=',', skip_header=1)
print(data.shape[0])