import numpy as np
import torch
import sys

data = np.loadtxt(sys.stdin, delimiter=' ')
tensor = torch.Tensor(data)
print(tensor.mean(dim=1).argmax().item())