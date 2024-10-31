import pandas as pd
import sys

df = pd.read_csv(sys.stdin)
names_count = df["Domains"].value_counts()
max_count = names_count.max()
max_popularity = names_count[names_count == max_count].sort_index()
for popularity, count in max_popularity.items():
    print(f"{popularity} {count}")
