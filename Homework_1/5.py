K = int(input())
M = int(input())
N1 = int(input())
N2 = int(input())

M2 = (M - N1) / (N2 - N1) * K
M1 = K - M2

print(int(M1), int(M2))
