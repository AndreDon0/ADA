import torch

N, M = map(int, input().split())
tensor1 = torch.tensor([list(map(int, input().split())) for _ in range(N)])
K, L = map(int, input().split())
tensor2 = torch.tensor([list(map(int, input().split())) for _ in range(K)])

print(torch.matmul(tensor1, tensor2.T).sum().item())
