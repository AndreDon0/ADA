import torch

n = int(input())
cursed_matrix = list([list(map(int, input().split())) for _ in range(n)])
max_len = max([len(L) for L in cursed_matrix])
for L in cursed_matrix:
    d = max_len - len(L)
    if d == 0:
        continue
    print(' '.join(map(str, L)) + " 0"*d)