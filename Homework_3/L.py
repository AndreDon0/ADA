def machine(n: int) -> int:
    s = str(n)
    if len(s) != 3:
        raise "The input is not a three digit number"
    else:
        n1 = int(s[0])
        n2 = int(s[1])
        n3 = int(s[2])
        s1 = str(n1 + n2)
        s2 = str(n2 + n3)
        array = sorted([s1, s2], reverse=True)
        return int(array[0] + array[1])


print(387)
"""
for i in range(100, 1000):
    if machine(i) == 1115:
        print(i))
        break
"""

