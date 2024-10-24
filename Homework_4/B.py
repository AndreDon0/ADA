import numpy as np
import sys

matrix = np.loadtxt(sys.stdin)
row_means = matrix.mean(axis=1, keepdims=True)
print(row_means)
new_matrix = matrix - row_means
print(str(new_matrix))
