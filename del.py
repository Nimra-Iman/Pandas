import pandas as pd
data = pd.read_csv('C:\\code_fun\\1_NUMPY\\Screentime - App Details.csv')


# print(data.head)
data = data.sort_values(by = 'Notifications', ascending=True)

data = data.reset_index(drop=True)
print(data.head)
