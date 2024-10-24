A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = A.intersection(B)
if C == {}:
    print(-1)
else:
    print(C)
