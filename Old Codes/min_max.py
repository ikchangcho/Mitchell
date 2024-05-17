import numpy as np

data = np.genfromtxt('../240508 Twist Values, Frenet-Serret Frame, Savistzky-Golay/twist_fr_sg_w3_p2.csv', delimiter=',', skip_header=1)
max = np.max(data)
min = np.min(data)
print(max, "\n", min)