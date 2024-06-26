import pandas as pd
data=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv")
print(data.index)  #yani data k indexes ka pta krna h (output: RangeIndex(start=0, stop=54, step=1) )

print(data.columns)  #to get the name of all columns

print(data.describe())  #dataset m numerical values ki min, max , avg, etc sab de ga

print(data.head(2))   # 1st 2 rows + header
print(data.tail(3))   # last 3 rows + header


print(data[:4])    # yani start s le kr 3rd index tak (n-1 yani 4-1 tak) + header 
print(data[2:4])   # yani 2 and 3 rows (yani index:2,3) + headerfiles

print(type(data))

print(data.index.array)  #to get all indices in the form of numpy array

# convert full data frame to index:
print()
print(data.to_numpy())   #2D array
# --------  2ND WAY -------
import numpy as np
v= np.asarray(data)
print(v)


# SORTING DATA IN DESCENDING ORDER:
print()
sorted_data= data.sort_index(ascending=False)
print(sorted_data)
print()
sorted_data= data.sort_values( by= "Notifications", ascending=False)
print(sorted_data)


# CHANGE THE SPCIFIC DATA:
print()
print()
data.loc[0,"Date"]="new_date"
print(data)
print()
print(data.loc[[2,3],["Date","Usage"]])  #yani date and usage ka 2 and 3 
                        # index ka data chayhye

print(data.loc[:,["Date","Usage"]])    #is s date and usage ka saara data mily ga



# ---- iLOC ----
print(data.iloc[0,1])    # yani 0th row and 1st column pr jo data pra h

# --- drop ---
print()
print()
print(data.drop("Date", axis=1)) #axis= 1 for column, yani poora date
# vala column drop kr do

print(data.drop(0, axis=0))  #axis=0 for row, yani 0 row drop kr do