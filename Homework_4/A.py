import numpy as np
import sys


matrix = np.loadtxt(sys.stdin)
if matrix.ndim == 1:
    print((matrix == 0).sum())
else:
    print((matrix == 0).all(axis=0).sum())