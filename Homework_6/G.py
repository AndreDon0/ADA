import pandas as pd
import sys

df = pd.read_csv(sys.stdin)
df["Age"] = 2021 - df["Year Published"]
print(round(df["Age"].mean(), 2))
