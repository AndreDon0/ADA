n = int(input())

if n % 2 == 1:
    print(0)
else:
    n = n // 2
    for i in range(0, n // 2 + 1):
        print(n - i * 2, i)
