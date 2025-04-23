import numpy as np
import torch
import sys

data = np.loadtxt(sys.stdin, delimiter=' ')
tensor = torch.IntTensor(data)
print(tensor[-2:,-2:].sum())