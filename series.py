# SERIES:  it is 1D array that is capable of storing various data types
import numpy as np
import pandas as pd

x=[6,7,8,9,10,111,12,3]
data=pd.Series(x)
# print(data)   #each element is 64 bit integer, means each element took 8 bytes of memory.

print("the value present at 5th index is :", data[5])


# we can also change the indexing of our data, default indexing starting from zero.
y=[2,3,4,5,6]
data_new=pd.Series(y, index=["a","b","c","d","e"], name="roll_numbers",
                   dtype="float")  #name s is poory data ka name rkha 
                            # dtype="float" krny s "y" list m dia gya saara data integer s
                            # float m convert ho jay ga 
# print(data_new)


# --------------------  when we pass dictionery instead of list:
students={"Nimra":4,"apsa":21, "mana":11, "taiba":23}
data_dict=pd.Series(students)
# print(data_dict)

language={"name":["python","c++","c"],"rank":[1,2,3], "property":[23,34,45]}
dat=pd.Series(language)
# print(dat)  # yhan pr dtype: object ay ga q k hm mixed data types ko use kr rhy hn
            # kuch integers hn or kuch string hn


# ------------------------  how to create data of single element
d=pd.Series(12)
# print(d)

d=pd.Series(12, index=[1,2,3,4,5])  # ab sary indexes pr 12 hi ho ga
# print(d)

# ------------------  why we use pandas data structures instead of numpy arrays:
a=np.array([1,2,3])
b=np.array([2,3,4,5,6])
# print(a+b)  #ab yhan error ay ga broadcast ka, dono arrays ki values equal nhi hn, yani 
# numpy missing values ko handle nhi krta

d=[1,2,3]
c=[2,3,4,5,6]
data1=pd.Series(d)
data2=pd.Series(c)
print(data1+data2)