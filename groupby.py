# agar ap k dataset m "names" k column m ek naam s bhhtt sary bachy hon or ap chahty hon
# k same naam k bacho ka data alag alag ho jay to hm groupby ko use krty hn

import pandas as pd
data=pd.DataFrame({"name":["joe","pop","bob","Aloce","Aloce","pop","pop","pop","Aloce"
                           ,"Aloce","Aloce","Aloce","joe","joe","joe"],
                    "age":[12,23,34,65,1,2,12,23,90,10,10,12,18,19,18],
                    "number":[1,2,3,4,5,6,7,8,9,10,56,43,21,56,89],
                     "SUBJECT":["math","eng","bio","phy","phy","math","eng","bio","phy","phy",
                                "math","eng","bio","phy","phy"]})
# print(data)
new_data=data.groupby("name")  #yani data to name ki basis pr group kr do
# print(new_data)  #this will give memory location.
# li=list(new_data)
# print(li)
# in order to get actual data, you have to use loop:
for x,y in new_data:
    print(x)  # x (the group name or value) 
    print(y)  # y (the corresponding subset of data).
    print()

# if i want k just mujy ek hi group ka data chahye:
print(new_data.get_group("Aloce"))

# to get minimum valued data from all groups
print()
print(new_data.min())
print(new_data.max())  #Aloce   age(90)   number(56)    subject(phy) yani, aloce k
# age valy column m maximum 90 tha, number valy column m maximum 56 tha or subjects
# vay column m maximum baar phy aya

print()
print()
print()
numeric_cols = data.select_dtypes(include='number').columns
print(new_data[numeric_cols].mean())    #mean of just numeric values







