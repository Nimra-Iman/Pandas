# replace function use hota h jab ap chaty hn k poori dataset m mojod vo value kisi or
# value s replce ho jay     
import pandas as pd
data=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv").head(10)

# --------  1st way to replace
print(data.replace(to_replace="Instagram", value="facebook"))  #yani poory dataset
# m instagram jhan bhi h vo facebook s replace ho jay.

# --------  2nd way to replace
print(data.replace("Instagram", "insta"))

print(data.replace([49,48,55],"1111"))

# --------  3rd way to replace (via regular expressions)
print(data.replace('[ 0-9 ,"A-Z" ]', "*", regex=True))  # yani 0 s 9 and A s Z tak koi bhi
        # a jay to us ko *  s replace krna h

# ---------  4th way (via dictionery)
print(data.replace({"Instagram":"FACEBOOK","08/26/2022":"DATED"}))

# ---------  5th way
print(data.replace(231, method="ffill"))  #yani 231 ko forward fill kia, yani 231 ki jga
                                            # 43 a jay ga
print(data.replace(231, method="bfill"))

print()
print()
# ---------  limit parameter:
print(data.replace( "Instagram","fb", limit=2  ))  # FutureWarning: The 'limit' keyword in
# DataFrame.replace is deprecated and will be removed in a future version.

# --------  inplace = True (yani permanent change)
# data.replace("Instagram","fb", inplace=True)
# print(data)

# ------------------------------  interpolate  --------------------------------------------
# to fill missing values automatically yani missing values ko fill krny k liye hmy fillna
# ki trah koi value na deni pry, to hm interpolate ka use krty hn,
#   interpolate only work with numerical data or y esy fill krta h k kisi column
# m jo value missing hoti h to vo missing k ilava vali values ko observe krta h or 
# us base pr missing values ko fill kr deta h

# No ML technique used behind it, there are different mathematical formuales
# behind every technoques. 

d=pd.read_csv("my_file1.csv")
print(d.interpolate(method="index", axis=0))  

 #ab is m data filling k bhhtt saaary methods aty hn, default
# method is linear, other methods are:  time, index, values, nearest, zero, slinear etc etc.

# axis=1 yani NaN ko fill krny ki observation row vis ho gi yani k agar hmary pas 3 columns
# hn , A   B   C , ab  B  m koi NaN h to B ki row m dekha jay ga yani B ki left and right 
# values ko observe kia jay ga or us ki base pr NaN ko fill kia jay ga. or y bhi
# zruri h k A and C numeric h tab hi vo B ki NaN ko numeric value s fill kr sky gy if axis=1

#  if axis= 0 kryn to column vis observation yani A k uper valy or neechy valy cell m dekha 
# jay ga or NaN ko fill kia jay ga, agar B k uper kuch bhi na hua to B ki NaN ko fill hi
# nhi jay ga and same is the case for axis=1 yani B ki left ya A ki NaN ki right m kuch
# na hua to fill nhi kia ja sky ga ( and AXIS=0 IS DEFAULT)

# -----------   limit parameter
print(d.interpolate(method="index", axis=0, limit=2, limit_direction='backward')) # agr ek column m 3 jga NaN aya to bas 2
# NaN fill kiye jay gy q k limit = 2 ki h

# ------------  limit direction
# agr ek column m 3 jga NaN aya to bas 2 NaN fill kiye jay gy q k limit = 2 ki h, ab hm
# yhan direction bhi da skty hn, direction can be "forward","backward","both". forward
# direction ka matlab y hua k just upr vali 2 NaN fill hon gi, backward ki matlab k
# neechy vali 2 fill hon gi and both ka matlab uper s bhi 2 or neechy s bhi 2 fill hon gi 
# agar NaN are more than or equal to 4. ,,,, q k limit-direction=forward s murad 
# asal m y h k agar ek column m 3 values missing thi to un missing vali s uper vali
# ki base pr neechy valo ko fill kia jay ga or ab agar limit = 2 kr di to bs uper valo ki
# base pr phli 2 ko hi fill kia jay ga ,  or agar limit-direction=backward kr dia to
# neechy valo ki base pr un missing ko fill kia jay ga or ab limit=2 kr di to neechy
# valo ki base pr uper vali sirf 2 NaN ko hi fill kia jay ga q k limit hi bas 2 ki h

# ------------------- limit_area:
# limit_area is used to restrict the area where interpolation is applied.

# limit_area='inside' applies interpolation only to the gaps that are bounded 
# by existing data points.

# limit_area='outside' applies interpolation only to the gaps that are at the 
# beginning or the end of the data.



