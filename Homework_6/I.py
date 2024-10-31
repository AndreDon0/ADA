import numpy as np
import pandas as pd
import sys
df = pd.read_csv(sys.stdin, sep=",")
shapes = df["ScreenResolution"].str.extract(r'(\d+)\s*x\s*(\d+)')
df["Width"] = shapes[0].astype(int)
df["Height"] = shapes[1].astype(int)
df["PPI"] = np.sqrt((df["Width"] ** 2) + (df["Height"] ** 2)) / df["Inches"]
print(round(df["PPI"].mean(), 2))

