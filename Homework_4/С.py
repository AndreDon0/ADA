import sys
import numpy as np


matrix = np.loadtxt(sys.stdin)
if matrix.shape[0] != 2:
    print("No solution")
else:
    vector_1 = matrix[0, :]
    vector_2 = matrix[1, :]
    mod_vector_1 = np.linalg.norm(vector_1)
    mod_vector_2 = np.linalg.norm(vector_2)
    if mod_vector_1 == 0 or mod_vector_2 == 0:
        print("No solution")
    else:
        similarity = np.dot(vector_1, vector_2) / mod_vector_1 / mod_vector_2
        print(round(similarity, 2))
