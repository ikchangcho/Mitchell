import numpy as np

data = {}
for i in range(1, 4):
    data[i] = np.genfromtxt(f'twist_ribbon{i}.csv', delimiter=',', skip_header=1)

tau = data[1][0]
print(tau)
