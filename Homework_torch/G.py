import torch

tensor = torch.tensor(list(map(float, input().split())))
shape = map(int, input().split())

print(tensor.reshape(list(shape)))