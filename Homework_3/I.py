s = input()

f1 = s.find("f")
if f1 == -1:
    print(-2)
else:
    s = s[f1 + 1:]
    f2 = s.find("f")
    if f2 == -1:
        print(-1)
    else:
        print(f2)
