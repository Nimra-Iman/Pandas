import pandas as pd

# series: name, index, dictionery, list
df = pd.Series([1,2,3,4,5], name = 'demo_date', index = [11,12,12,12,12])
# print(df)

data = pd.Series({'name':1, "name2":2})
# print(data)

# ----------------------------------------------------------------------------------------------------
d = pd.DataFrame(([1,2,3,4],[6,7,8,9]),  index = [1,2], columns = [1,2,3,4])
print(d)