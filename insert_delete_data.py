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
# print(datas)



# IF YOU WANT K AP EK LIMIT TAK HI NEW COLUMN M VALUES DAALMNA CHAHTY HN OR BAKI KI VALUES
# MISSING RKHNA CHATY HN( YANI US KI JGA NaN SHOW HO GA), TO US O ESY KRY GY:

x1=pd.Series([23,34])
datas["new_column"]=x1
# print(datas)

datas["new_columns"]=datas["age"][:2]  # yani hm chahty hn k age column vala data hi us k
# ander jay but saara na jay to hm us ki slicing kry gy
# print(datas)


#  ---------------------  DELETE A SPECIFIC COLUMN:
deleted_col=datas.pop("new_column")
print("the deleted column is :\n",deleted_col )
print("new data after deleteing the column is :\n", datas)

# ------------  2ND WAY ------------
del datas["new_cols"]
print(datas)