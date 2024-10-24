from math import sin, cos


def f(x):
    return x ** 2 + 15 * cos(x)


def d_f(x):
    return 2 * x - 15 * sin(x)


x0, N, lam = input().split()
x0, N, lam = float(x0), int(N), float(lam)

for _ in range(N):
    x0 -= lam * d_f(x0)

print(round(x0, 4))
