from frames import *
import matplotlib.pyplot as plt

# Curvature 1, Torsion 1 helix
N = 1000
r1 = np.zeros((N, 3))
r2 = np.zeros((N, 3))
r3 = np.zeros((N, 3))
for i in range(N):
    r1[i] = [np.cos(i * 10 / N), np.sin(i * 10 / N), 0.5 * i * 10 / N]
    r2[i] = [0.5 * np.cos(i * 10 / N), 0.5 * np.sin(i * 10 / N), 0.5 * i * 10 / N]
    r3[i] = [0.5 * np.cos(i * 10 / N), 0.5 * np.sin(i * 10 / N), 0]

d1, d2, d3, K, tau1, Tw = frenet_serret_frame2(r1)
d1, d2, d3, K, tau2, Tw = frenet_serret_frame2(r2)
d1, d2, d3, K, tau3, Tw = frenet_serret_frame2(r3)
#d1, d2, d3, K, tau, Tw = frenet_serret_frame_savitzky_golay(r, 20, 2)

# print(' d1\n', d1[:5], '\n', 'd2\n', d2[:5], '\n', 'd3\n', d3[:5])
# print('Torsion: ', tau[200:220])
# #print('Curvature: ', K[:10])
# print('Orthogonality')
# for j in range(5, 9):
#     print(np.inner(d2[j], d3[j]))


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.scatter(r1[:, 0], r1[:, 1], r1[:, 2])
ax.scatter(r2[:, 0], r2[:, 1], r2[:, 2])
plt.tight_layout()
plt.show()

# plt.plot(tau1)
# plt.plot(tau2)
# plt.xlabel('s')
# plt.ylabel('Torsion')
# #plt.ylim([0.3, 0.5])
# plt.title('Torsion of Helices')
# plt.show()

