# they are 2D data structures and they have multiple columns and rows.

import pandas as pd
a={"roll_no":[1,2,3,4], "name":["nimra","iman","fatima","humiara"]}
data=pd.DataFrame(a)
# print(data)

# --------  IN ORDER TO GET JUST 1 COLUMN FROM "a" in DATA:
a={"roll_no":[1,2,3,4], "name":["nimra","iman","fatima","humiara"], "age":[20,21,23,11]}
data=pd.DataFrame(a, columns=["name"])
# print(data)


# --------  PASS NEW INDEXES:
a={"roll_no":[1,2,3,4], "name":["nimra","iman","fatima","humiara"], "age":[20,21,23,11]}
data=pd.DataFrame(a, columns=["name"], index=["a","b","c","d"])
print(data)


# ---------  TO GET VALUES AT A SPECIFIC INDEX:
a={"roll_no":[1,2,3,4], "name":["nimra","iman","fatima","humiara"], "age":[20,21,23,11]}
data=pd.DataFrame(a, columns=["name", "age"], index=["a","b","c","d"])
# print(data)
############################ print("data element present at :", data.iloc[0][1] )   #row position and column position
############################ print("data element present at :", data.loc["a"][1] )  #index label name then row position


# ------------  CREATE DATA FRAME USING LIST OF LIST
x=[[11,22,33,44],[66,55,77,88]]
data=pd.DataFrame(x)
print(data)  # this will give column name 0 ,1 ,2, 3

x=[[11,22,33,44],[66,55,77,88]]
data=pd.DataFrame(x, columns=["A","B","C","D"])
print(data)




# --------------  CREATE DATA FRAME USING Series
x={"name":pd.Series(["nimra","iman","kinza"]), "age":pd.Series([20,21,23])}
data=pd.DataFrame(x)
# print(data)    #series s jab data frames ko create krty hn to "index =" nhi de skty


# DATA FRAMES KO USE KRTY HUY HM DATA KA NAME NHI RKH SKTY 