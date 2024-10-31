import pandas as pd
import sys

df = pd.read_csv(sys.stdin)
df['Domains'] = df['Domains'].fillna('').str.split(',')
rating_strategies = df[df["Domains"] == "Strategy Games"]["Rating Average"]
rating_strategies = rating_strategies.str.replace(',', '.', regex=False).astype(float)
print(rating_strategies.dropna().mean())