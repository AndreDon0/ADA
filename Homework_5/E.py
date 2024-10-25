import numpy as np
import sys


def max_sum_in_str(matrix: np.ndarray) -> np.ndarray:
    sum_array = matrix.sum(axis=1)
    max_value = sum_array.max()
    return np.argwhere(sum_array == max_value).flatten()


arr = max_sum_in_str(np.loadtxt(sys.stdin))
np.savetxt(sys.stdout, arr, fmt='%d', delimiter=' ', newline=' ')
