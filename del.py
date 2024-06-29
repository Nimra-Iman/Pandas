import pandas as pd
data=pd.DataFrame({"name":["joe","pop","bob","Aloce","Aloce","pop","pop","pop","Aloce"
                           ,"Aloce","Aloce","Aloce","joe","joe","joe"],
                    "age":[12,23,34,65,1,2,12,23,90,10,10,12,18,19,18],
                    "number":[1,2,3,4,5,6,7,8,9,10,56,43,21,56,89],
                     "SUBJECT":["math","eng","bio","phy","phy","math","eng","bio","phy","phy",
                                "math","eng","bio","phy","phy"]})

print(data.isna().sum())