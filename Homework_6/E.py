import pandas as pd
import sys

pd = pd.read_csv(sys.stdin, sep=',')
age_more_35 = pd[pd["Возраст"] > 35]["Имя"]
print(*age_more_35)
