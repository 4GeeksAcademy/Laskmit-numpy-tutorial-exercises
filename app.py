# 002
import numpy as np

# 003
# print(np.__version__)
# print(np.show_config())

# 004
# print(np.zeros(10))

# 005
# zeros = np.zeros(10)
# mem_size = zeros.itemsize * zeros.size
# print(mem_size)

# 006
# np.info(np.add)

# 007
# arr = np.zeros(10)
# arr[4] = 1

# print(arr)

# 008
# arr = np.arange(10, 50)
# print(arr)

# 009
# arr = np.arange(0, 10)
# print(arr[::-1])

# 010
# arr = np.arange(0, 9)
# print(np.reshape(arr, (3, 3)))

# 011
# arr = np.array([1,2,0,0,4,0])
# print(np.nonzero(arr))

# 012
# matrix = np.eye(3)
# print(matrix)

# 013
# arr = np.random.random(3)
# print(arr)

# 014
# arr = np.random.random(10)
# print(arr.max())

# 015
# arr = np.random.random(10)
# print(arr.mean())

# 016
# matrix = np.ones((5, 5))
# matrix[1:-1,1:-1] = "0"
# print(matrix)

# 017
# matrix = np.ones((3, 3))
# padded_matrix = np.pad(matrix, pad_width=1)
# print(padded_matrix)

# 018
# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(np.nan in set([np.nan]))
# print(0.3 == 3 * 0.1)

# 019
# matrix = np.arange(0, 9).reshape(3, 3)
# print(np.diag(matrix))

# 020
matrix = np.zeros((8, 8))
matrix[1::2, ::2] = 1
matrix[::2, 1::2] = 1
print(matrix)
