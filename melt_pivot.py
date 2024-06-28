
# In pandas, pivot and melt are used for reshaping DataFrames. They are powerful
#  tools for transforming data into different formats, which can be essential for 
# data analysis and visualization.

import pandas as pd
data=pd.DataFrame({"roll_no":[1,2,3,4],"name":["ana","joe","bob","jan"],"age":[15,16,17,18]})
print(pd.melt(data, id_vars="roll_no", var_name="Col_name", value_name="raqam"))  #melt convert dataframe from wide format to long formate
# id_vars is used jab ap kisi column name ko id k tor pr use krna chahty hn.

#  roll_no  variable  value , output m esy show ho rha h, hm chahty hn k variable ki jga
# koi or word a jayto is liye hm n var_name use kia. or "value" ka name change
# krna h to value_name likhyn gy 

print()
print()
print()
# -----------------  pivot  ---------------------
data=pd.DataFrame({"roll_no":[1,2,3,4,5,6],"name":["ana","joe","bob","jan","joe","joe"],
                   "age":[15,16,17,18,18,16],"class":[2,3,4,5,2,3]})
# print(pd.pivot(data, index="roll_no", columns="name", values="age"))
# values in index can never be duplicate.
# values="age" yani sirf age ki values show ho just

print()
print()
print()
#  to perform different arithematic operations
data=pd.DataFrame({"roll_no":[1,2,3,4,5,6],"name":["ana","joe","bob","jan","joe","joe"],
                   "age":[15,16,17,18,18,16],"class":[2,3,4,5,2,3]})

print(data.pivot_table(index="roll_no", columns="name", aggfunc="mean" , margins="True"))


