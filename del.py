import pandas as pd


a={"roll_no":[1,2,3,4], "name":["nimra","iman","fatima","humiara"], "age":[20,21,23,11]}
# data=pd.DataFrame(a, columns=["name", "age"], index=["a","b","c","d"])
data=pd.DataFrame(a, index=["a","b","c","d"])
print(data)
print("data element present at :", data.iloc[[0,2],2] ) 

print()
print()
print()
print()
# loc function gives value on the basis of index:
# print(data.loc['a'])
# print(data.loc[['a','b'],'name'])




