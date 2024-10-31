import pandas as pd
import sys

df = pd.read_csv(sys.stdin, sep=",")
df_nan = df.isna().sum().reset_index()
df_nan.columns = ["Название_колонки", "Количество_NaN"]
df_nan.to_csv(sys.stdout, sep=',', header=True, index=False)
