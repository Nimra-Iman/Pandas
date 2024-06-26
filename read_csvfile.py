import pandas as pd
# file=pd.read_csv("my_csvfile1.csv")
# print(file)


file=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv", nrows=3,
                  usecols=["Notifications"])  #baaz oqat formward slashes 
        # jab k double back slashes use hoti hn.
# print(file)

# nrows=1 (to get a specific row from the dataset) is 
# s yani nrows=1 s hust ek row show ho gi + header row
# nrows=3 (phli 3 rows show hon gi and The header row is still included
#  as usual, so the columns are correctly named.
# nrows=2 s murad phli do rows + header row

# usecols=["Notifications"]  , usecols ki list m jin columns ka nem likhyn gy just vo columns 
    # show hon gy, ab m n nrows=3 kia hua h to ab usecols ki list m pas hue columns ki 1st 
    # three rows hi show hon gi.,,,,  usecols=[0] esy bhi kr skty hn, is s 0th column show ho ga, 
    # yani vo column jis ka index number 0 h, yani k date vala column

# ---------  SKIP A PARTICULAR ROW:
file=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv", skiprows=[0,1]) 
# print(file)

# skiprows=[0,1] krny s 0th and 1st row skip ho gi, following both rows will be skipped:  
#                 Date  Usage  Notifications  Times opened        App
# 0   08/26/2022     38             70            49  Instagram

# ek baat ka khial rhy:  When using the skiprows parameter in pd.read_csv(), the values
#  you provide correspond to the line numbers in the file (0-indexed), not the actual
#  index values of the DataFrame, e.g, agar ap k indexes 19 s start ho rhy hn, ap ek
# header vali row(jis row m columns k name likhy hoty) or us s agli row or us s bhi agli row
# ko skip krna chahty to esy kryn gy:  skiprows[0,1,2] , is s header , index:19 and index:20
# vali rows skip hon gi.

# -------  agar ap khali skiprows=0 likhty ho (unlike this: skiprows=[0]) , yani list k
    # bagher pass krty ho to koi row skip nhi ho gi.


# -----------  MAKING A SECIFIC COLUMN AN INDEX:
# yani abhi tak hmary pas index default index a rhi thi, 0 ,1,2 etc, hm chahty hn k hmara 
# koi specific column hi hmara index bny, to hm  index_col ko use kryn gy
file=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv",index_col="Date" ) 
# print(file)


# -----------------  CHANGING HEADER:
# if you want k koi specific row header ban jay:
file=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv", header=2) 
# print(file)     # row number 2, yani starting from row 0(header vali), then row 1 then 
                # row 2 , row 2 vali row header ban jay gi.


# -----------  TO CHNAGE THE NAME OF COLUMNS:
file=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv",
                 names=["col1", "col2","col3","col4","col5"]) 
# print(file) 

# ------------  REMOVING HEADER:
# header=None krny s headers khtm ho kr, 0,1,2 ... show hon gy
file=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv",
                 header=None) 
# print(file)


# -----------   CHANGING THE DATATYPE:
# dtype={"Notifications":"float"} yani mujy notifications ko float m convert krvana h
file=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv", dtype={"Notifications":"float"}) 
print(file)

# nrows, usecols, skiprows, index_col, header=2, names, header=None, prefix, dtype.