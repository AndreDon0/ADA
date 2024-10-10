def A(n, m):
    if n == 0:
        return m + 1
    if m == 0:
        return A(n - 1, 1)
    else:
        return A(n - 1, A(n, m - 1))


N, M = map(int, input().split())
print(A(N, M))
