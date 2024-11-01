import pandas as pd
import sys

df = pd.read_csv(sys.stdin)

df["Rating Average"] = df["Rating Average"].str.replace(',', '.', regex=False).astype(float)

strategy_games = df[df['Domains'].str.contains('Strategy Games', case=False, na=False)]
average_rating = strategy_games['Rating Average'].mean()

print(round(average_rating, 2))
