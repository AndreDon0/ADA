import numpy as np
import pandas as pd
import sys
df = pd.read_csv(sys.stdin, sep=",")
df = pd.concat([
    df,
    df["ScreenResolution"].str.extract(r'(?P<Width>\d+)x(?P<Height>\d+)').astype("int")], axis=1)
df["PPI"] = np.sqrt((df["Width"] ** 2) + (df["Height"] ** 2)) / df["Inches"]
print(round(df["PPI"].mean(), 2))

