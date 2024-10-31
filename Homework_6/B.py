import pandas as pd
import sys

df = pd.read_csv(sys.stdin, sep=",")
names_count = df["Имя"].value_counts()
max_names_count = names_count[names_count == names_count.max()].sort_index()
max_names_count.to_csv(sys.stdout, sep=' ', header=False)
