import pandas as pd
import sys

df = pd.read_csv(sys.stdin, sep=",", header=None)
print(*df.shape, sep="\n")
