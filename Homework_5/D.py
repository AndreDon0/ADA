import numpy as np
import sys


def symetric(matrix: np.ndarray) -> bool:
    return np.array_equal(matrix, matrix.T)


print(symetric(np.loadtxt(sys.stdin)))
