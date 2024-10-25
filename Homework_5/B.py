import numpy as np
import sys


def make_chess_matrix(N: int) -> np.ndarray:
    chess_matrix = np.zeros((N, N), dtype=int)
    np.where(chess_matrix == 0, -1, chess_matrix)
    for i in range(1, N, 2):
        chess_matrix += np.eye(N, k=i, dtype=int)
        chess_matrix += np.eye(N, k=-i, dtype=int)
    return chess_matrix


np.savetxt(sys.stdout, make_chess_matrix(int(input())), fmt='%d')
