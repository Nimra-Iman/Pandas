import pandas as pd

# series: name, index, dictionery, list

d=[1,2,3]
c=[2,3,4,5,6]
data1=pd.Series(d)
data2=pd.Series(c)
print(data1+data2)