def distance(x1, y1, x2, y2):
    from math import sqrt
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(round(distance(x1, y1, x2, y2), 4))
