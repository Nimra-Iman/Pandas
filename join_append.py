import pandas as pd
# join is used to combine two DataFrames based on their index or a key column.

data1=pd.DataFrame({"id":[1,2,3,4],"name":["ana","joe","bob","jan"]},index=["a","b","c","d"])

data2=pd.DataFrame({"roll_no":[1,13,41],"age":[15,17,18]}, index=["a","b","c"])

# ab agar m yhan dono dataframes k indexes different krti to y join na hota
new=data1.join(data2)
# print(new)




# --------------------  2nd condition
data1=pd.DataFrame({"roll_no":[13,41],"age":[15,17]}, index=["a","b"])
data2=pd.DataFrame({"id":[1,2,3,4],"name":["ana","joe","bob","jan"]},index=["a","b","c","d"])

new_data=data1.join(data2, how="right")
# print(new_data)

# Inner Join (intersection): --> This returns only the rows with indices that are present in both DataFrames.
# left join (default) : --> is m left dataframe k saary indices ay gy or right ki vo rows ayn gy jin k
# indexes left valy indices s match ho rhy hn, jo match nhi ho rhy un ki jga NaN.
# Outer Join (union)--> : This returns all rows from both DataFrames. For rows that do not have a match, the 
# result will contain NaN for the columns from the DataFrame without a match. 
# same for right (k right valy saary or, left valy matching)

# -----------------------  3rd casse:
data1=pd.DataFrame({"roll_no":[13,41],"age":[15,17]}, index=["a","b"])
data2=pd.DataFrame({"roll_no":[1,2,3,4],"name":["ana","joe","bob","jan"]},index=["a","b","c","d"])
n=data1.join(data2, lsuffix="_phla", rsuffix="_phla")  
# print(n)
# yhan error ay ga agr hm sufix na den , q k join error deta h jab hmary datafames
# m kisi column ka name same ho, is liye lsuffix ya rsuffix k zrye hm kisi ek column ka
# name change kr dety hn, ap chahy to lsuffix and rsuffix dono use krskty or chahy 
# lsuffix and rsuffix dono m same values hon to phir bhi error nhi ay ga q k ab y dono
# columns different hn



# ---------------  append ---------------
# agar column name same a jay dono dataframes m to append error nhi deta
data1=pd.DataFrame({"roll_no":[13,41],"age":[15,17]}, index=["a","b"])
data2=pd.DataFrame({"roll_no":[1,2,3,4],"name":["ana","joe","bob","jan"]},index=["a","b","c","d"])
new=data1._append(data2, ignore_index=True)
print(new)