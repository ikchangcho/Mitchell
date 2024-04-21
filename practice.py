import numpy as np

x = [[1, 2, 3], [4, 5, 6]]
x = x / np.linalg.norm(x, axis=1, keepdims=True)
print(x)
print(np.linalg.norm(x, axis=1, keepdims=True))
