import sys
import numpy as np


min_similarity = 1
for vector in sys.stdin:


similarity = np.dot(vector_1, vector_2) / np.linalg.norm(vector_1) / np.linalg.norm(vector_2)
if 0 <= similarity <= 1:
    print(round(similarity, 2))
else:
    print("No solution")
