# merge() used to merge two dataframes
import pandas as pd
data1=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
data2=pd.DataFrame({"A":[1,2,3,4],"C":[15,16,17,18]})
print(pd.merge(data1,data2, on="A"))  #merge ko use krny k liye zruri h k 2 data frames m
# s koi ek column common ho or us common valy column m "on" m pass krna h. agar "on"
# ko pass nhi kryn gy or ek hi common column ho ga to output theek ay gi, python
# khud hi detect kr le ga common column ko but agar ek s ziada column common huy or
# "on" pass na kraya yani na btaya k kis common column ki base pr merge krna h to python
# ambiguity ka shikar ho ga.

print(pd.merge(data2, data1, on="A")) #is s ab data2 k columns phly ay gy


# -------------------------------------------
data1=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
data2=pd.DataFrame({"A":[1,2,3,41],"C":[15,16,17,18]})
print(pd.merge(data1,data2, on="A"))  #A vala data end s different h, to jhan tak common h 
                # vhan tak merge ho ga


# ---------------------------------------
# -------------------  Types of Joins
# You can specify different types of joins with the how parameter:

# inner (default): Only include rows with keys in both dataframes.
# left: Include all rows from the left dataframe and matching rows from the right dataframe.
# right: Include all rows from the right dataframe and matching rows from the left dataframe.
# outer: Include all rows from both dataframes, filling in NaN where there are no matches.
data1=pd.DataFrame({"id":[1,2,3,4],"name":["ana","joe","bob","jan"]})
data2=pd.DataFrame({"id":[1,2,13,41],"age":[15,16,17,18]})
print(pd.merge(data1,data2, on="id", how="left"))  # left join h yani left vala sara table(dataframe)
# or right table s just matching , yani jab id 1 ho gi to name "ana" ho ga or age 15 ho gi
# so yani jab id 2 ho gi to name "joe" ho ga and age 16 ho gi, similarly, jab id 3 ho gi
# to name "bob" ho ga but id # 3 doosry tabkle m h hi nhi yani doosry table m id # 3
# k across koi bhi age nhi given to vhan NaN a jay ga and similarly jab id 4 ho gi to
# name "jan" ho ga and age NaN q k doosry table m given hi nhi.
print()
print()
# ---------------- indicator=True (yani kon ca missing h or kon ca merge hua h)
data1=pd.DataFrame({"id":[1,2,3,4],"name":["ana","joe","bob","jan"]})
data2=pd.DataFrame({"id":[1,2,13,41],"age":[15,16,17,18]})
print(pd.merge(data1,data2, on="id", how="outer", indicator=True)) 


# ----------------  left_index, right_index
data1=pd.DataFrame({"id":[1,2,3,4],"name":["ana","joe","bob","jan"]})
data2=pd.DataFrame({"id":[1,2,13,41],"name":[15,16,17,18]})
print(pd.merge(data1,data2, left_index=True, right_index=True, suffixes=("phlaT","dusraT")))  #yani agar dono tables
# k columns k name same hn to in s pta lag jay ga k kis dataframe ki kon c value h
# ----  phlaT yani phly table  
# ----  dusraT yani dusra table

# 

# --------------------  CONCAT  ----------------------------------------
d1=pd.Series([1,2,3,4,5])
d2=pd.Series([11,12])   
print(pd.concat([d1,d2], axis=1))   # chahy same length na bhi ho
# concat kisi common column ki base pr concatenation nhi krta
# ----> axis=0 is default, yani concat is trah s ho ga k izafi rows bny gi, or axis=1
# kro to izafi columns bny gy

print()
print()
data1=pd.DataFrame({"id":[1,3],"name":["bob","jan"]})
data2=pd.DataFrame({"id":[1,2,13,41],"name":[15,16,17,18]})
print(pd.concat([data1,data2], axis=1, join="outer", keys=["d1","d2"]))

# ab jo missing data NaN s show ho rha tha us ko htany k liye join="inner" likhy gy;
# join can be "inner", "outer";; "inner" means intersection( yani just common) and 
# "outer" means union yani sab data dikhay ga chay NaN vala ho ya chahy us k bagher vala
# ---> "inner" krny s NaN vali poori row hta de ga, chaybrow m ek hi NaN q na ho
# ----->>> keys=["d1","d2"] yani 2 dataframes merge huy hn, yani phly valy data k uper ek
# indication type lga di k y d1 h or doosra yhan s start ho rha h y d2 h.



d1=pd.DataFrame([1,2,3,4,5], columns=["A"])
d2=pd.DataFrame({"A":[12,13,12,12,12],"B":[67,67,54,32,12]})
print(pd.concat([d1,d2], keys=["a","b"], axis=0))





