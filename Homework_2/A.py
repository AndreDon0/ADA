n, m = map(int, input().split())
convolution = list([list(map(int, input().split())) for _ in range(m)])
w, h = map(int, input().split())
image = list([list(map(int, input().split())) for _ in range(h)])
tensor = list(list([0 for _ in range(w - n + 1)]) for _ in range(h - m + 1))

for i in range(w - n + 1):
    for j in range(h - m + 1):
        s = 0
        for i_t in range(n):
            for j_t in range(m):
                s += convolution[i_t][j_t] * image[i + i_t][j + j_t]
        tensor[i][j] = s

for _ in tensor:
    print(*_)
