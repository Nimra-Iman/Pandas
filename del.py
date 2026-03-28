import pandas as pd
data = pd.read_csv('weather2.csv')


print(pd.pivot_table(data, index='city', columns='date', aggfunc='mean', margins=True))

