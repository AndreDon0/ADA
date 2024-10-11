def power_multiple_solutions(*abc):
    a, b, c = abc
    if a == 0:
        if b == 0:
            if c == 0:
                return -1
            else:
                return 0
        else:
            return 1
    else:
        D = b ** 2 - 4 * a * c
        if D < 0:
            return 0
        elif D == 0:
            return 1
        else:
            return 2


a, b, c, d = map(int, input().split())
print(power_multiple_solutions(a, b, c - d))
