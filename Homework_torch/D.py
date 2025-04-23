import torch

features = torch.tensor(list(map(float, input().split())))
weights = torch.tensor(list(map(float, input().split())))
bies = torch.tensor(float(input()))

s = (features * weights).sum() + bies
print(torch.tensor([1 / (1 + (s.exp())**-1)]))
