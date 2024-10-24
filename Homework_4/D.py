import numpy as np
import sys

k = int(input())
matrix = np.loadtxt(sys.stdin)
n1, m1 = np.shape(matrix)
matrix = np.pad(matrix, ((0, n1 - k * (n1 // k)), (0, m1 - k * (m1 // k))), mode='constant', constant_values=0)

n2, m2 = np.shape(matrix)
new_matrix = np.zeros((n2 // k, m2 // k))

for i in range(n2 // k):
    for j in range(m2 // k):
        new_matrix[i, j] = matrix[i * k:(i + 1) * k, j * k:(j + 1) * k].sum()

np.savetxt(sys.stdout, new_matrix, fmt='%d', delimiter=' ')
