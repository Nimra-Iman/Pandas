import pandas as pd
x={"name":["nimra","imna","kinza"], "age":[21,23,21]}
datas=pd.DataFrame(x)
# print(datas)

# -------------------------in order to insert new column in the data:

# phly number pr y btana h k new_column kis index pr daalna h, then us ka name kia h and
# then us m data kia jay ga , or is column m paas kiye gay data ka size vhi ho
# jo pichly columns m h, yani data kam ya ziada na daalo, q k error ay ga
new_data=pd.Series([23,34,45])
datas.insert(1,"new_col",new_data)  #yani mujy output m y column "1" index pr show ho
datas.insert(3, "new_cols",datas["age"])
print(datas)



# IF YOU WANT K AP EK LIMIT TAK HI NEW COLUMN M VALUES DAALMNA CHAHTY HN OR BAKI KI VALUES
# MISSING RKHNA CHATY HN( YANI US KI JGA NaN SHOW HO GA), TO US O ESY KRY GY:

x1=pd.Series([23,34])
datas["new_column"]=x1
print(datas)

datas["new_columns"]=datas["age"][:2]  # yani hm chahty hn k age column vala data hi us k
# ander jay but saara na jay to hm us ki slicing kry gy
print(datas)


#  ---------------------  DELETE A SPECIFIC COLUMN:
deleted_col=datas.pop("new_column")
print("the deleted column is :\n",deleted_col )
print("new data after deleteing the column is :\n", datas)

# ------------  2ND WAY ------------
del datas["new_cols"]  #via "del" keyword, column is permanantly deleted, so that's why, 
                    # deleted column cannot be shown in output.
print(datas)



# -----------------------   IMPORTANT --------------------------------------------


data = pd.DataFrame({'name':[1,2], 'date':[1,2]}, index=[1,2])
data.insert(1,'new', pd. Series([1,2]))
print(data) 
#    name  new  date
# 1     1  2.0     1
# 2     2  NaN     2    NaN is liye aya q k pandas indexes ki base pr values ko align krta h, 
# yani is time dataframe k indexes [1,2] hn or series k bydefault indexes [0,1] hn, ab panda
# insert krty huy dekhy ga k dataframe ka index 1 h to series k index 1 pr kia value pri h, 
# jo k 2 h asl m, ab agy dekhy ga k jab datafrmae ka index 2 tha to series k index k index 2 pr
# kia tha, to koi value nhi thi is liye NaN a gya,, if we do following:
data = pd.DataFrame({'name':[1,2], 'date':[1,2]}, index=[11,21])
data.insert(1,'new', pd. Series([1,2]))
print(data)    #'new' column m dono jga NaN ay ga,, better to use folowing:

data = pd.DataFrame({'name':[1,2], 'date':[1,2]}, index=[1,2])
data.insert(1,'new', pd. Series([1,2], index=[1,2]))
print(data)
# Conclusion: 
# NaN isliye aya kyun ke Pandas index ki base par values ko align karta hai.

# DataFrame ke index [1,2] thay aur Series ke default index [0,1] thay.

# Jab Pandas insert karta hai to wo index match karta hai:
# - DF index 1 → Series index 1 → value mil gayi (2)
# - DF index 2 → Series me index 2 nahi tha → NaN

# Agar indexes bilkul match na karein (e.g. [11,21]) to dono jagah NaN aata hai.

# Solution: Series ka index DataFrame ke index ke barabar rakho.