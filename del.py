import pandas as pd


data = pd.read_csv("weather2.csv")
print(data)
d = pd.pivot_table(data, index="date", columns="city")
print(d)








