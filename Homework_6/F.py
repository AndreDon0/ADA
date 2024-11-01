import pandas as pd
import sys

df = pd.read_csv(sys.stdin)

domains = df["Domains"]
domains = domains.str.split(",")
domains = domains.explode()

names_count = domains.value_counts()
most_popular = names_count[names_count == names_count.max()].sort_index()

for popularity, count in most_popular.items():
    print(f"{popularity} {count}")
