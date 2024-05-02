from functions import *

# Curvature 1, Torsion 1 helix
N = 100000
r = np.zeros((N, 3))
for i in range(N):
    r[i] = [0.5 * np.cos(i * 10 / N), 0.5 * np.sin(i * 10 / N), 0.5 * i * 10 / N]

#d1, d2, d3, K, tau = frenet_serret_frame2(r)
d1, d2, d3, K, tau = frenet_serret_frame_savitzky_golay(r, 20, 2)

print(' d1\n', d1[:5], '\n', 'd2\n', d2[:5], '\n', 'd3\n', d3[:5])
print('Torsion: ', tau[100:112])
#print('Curvature: ', K[:10])
print('Orthogonality')
for j in range(5, 9):
    print(np.inner(d2[j], d3[j]))


# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1, projection='3d')
# ax.scatter(r[:, 0], r[:, 1], r[:, 2])
# plt.show()

