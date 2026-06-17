import pandas as pd
data1=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,8,5]})
data2=pd.DataFrame({"A":[1,2,3,4],"C":[15,16,17,18]})

print(data1)
# data = data1.merge(data2, how = 'outer')
# print(data)