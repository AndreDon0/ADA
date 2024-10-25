import numpy as np
import sys


def has_zero_column(matrix: np.ndarray) -> bool:
    return (matrix == 0).all(axis=0).sum() > 0


print(has_zero_column(np.loadtxt(sys.stdin)))
