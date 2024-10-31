import numpy as np
import pandas as pd
import sys

df = pd.read_csv(sys.stdin, sep=",")
print(*np.sort(df["Имя"].unique()))
