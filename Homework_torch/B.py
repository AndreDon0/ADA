import torch

N, M = map(int, input().split())
tensor = torch.tensor([list(map(int, input().split())) for _ in range(N)])
limit = int(input())

print(tensor[tensor > limit].sum())