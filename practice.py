import numpy as np

j = 1
for i in range(1, 61):
    torsion = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240427 Torsion/torsion_time{i}.csv')
    twist_rate = np.genfromtxt(f'/Users/ik/Pycharm/Mitchell/240427 Twist Rate, Ribbon Frame {j}/twist_rate_ribbon{j}_time{i}.csv')
    new = twist_rate - torsion
    np.savetxt(f'')

