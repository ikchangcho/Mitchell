import numpy as np

twist_rates = {}
for j in range(1, 5):
    twist_rates[j] = np.genfromtxt(f"twist_rate_ribbon{j}.csv", delimiter=",", skip_header=1)

average1= (twist_rates[1]+twist_rates[2]+twist_rates[3]+twist_rates[4])/4
average2= np.genfromtxt("twist_rate_average.csv", delimiter=",", skip_header=1)
print(average1 - average2)