import pandas as pd

# --> TO CONVERT NUMERICAL DATA TO CATEGORICAL, WE USE pd.cut(data['months'], bins = 5), 
# suppose we have month variable showing how much months you work with us, data is numerical
# so it wil convert it into 5 bins of (0-5), (6-10) months etc etc 

# data=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv")
# print(data.index)  #yani data k indexes ka pta krna h (output: RangeIndex(start=0, stop=54, step=1) )
# print(data.index.array)  #to get all indices in the form of numpy array

# print(data.columns)  #to get the name of all columns

# print(data["App"].value_counts())  #  Returns the counts of how many times each
#                 # unique value occurs in this column

# print(data.isna().sum()) #Shows how many missing values there are on each column.



# print(data.describe())  #dataset m numerical values ki min, max , avg, etc sab de ga

# print(data.head(2))   # 1st 2 rows + header
# print(data.tail(3))   # last 3 rows + header


# print(data[:4])    # yani start s le kr 3rd index tak (n-1 yani 4-1 tak) + header 
# print(data[2:4])   # yani 2 and 3 rows (yani index:2,3) + headerfiles

# print(type(data))


# # convert full data frame to array:
# print()
# print(data.to_numpy())   #2D array 
# # --------  2ND WAY -------
# import numpy as np
# v= np.asarray(data)
# print(v)


# # SORTING DATA IN DESCENDING ORDER:
# print()
# sorted_data= data.sort_index(ascending=False)
# print(sorted_data)
# print()
# sorted_data= data.sort_values( by = "Notifications", ascending=False)
# print(sorted_data)


# # CHANGE THE SPECIFIC DATA:
# print()
# print()
# data.loc[0,"Date"]="new_date"
# print(data)
# print()
# print(data.loc[[2,3],["Date","Usage"]])  #yani date and usage ka 2 and 3 
#                         # index ka data chayhye

# print(data.loc[:,["Date","Usage"]])    #is s date and usage ka saara data mily ga



# # ---- iLOC ----
# print(data.iloc[0,1])    # yani 0th row and 1st column pr jo data pra h

# # --- drop ---
# print()
# print()
# print(data.drop("Date", axis=1)) #axis= 1 for column, yani poora date
# # vala column drop kr do

# print(data.drop(0, axis=0))  #axis=0 for row, yani 0 row drop kr do



# # data['column_name'].isin(["some_list"])
# # Returns a Series object filled with True or False by checking if the values of the
# # column exists in the given list

# data.drop_duplicates()  # Returns a dataframe where rows with duplicate values is 
# # removed to only leave one copy.

# data.drop_duplicates(['column_name'])  # # Same as previous but only takes the given
# # column to check for duplicates values. You can give it more than one column name.


# data.reset_index()
# #  Resets the index to be ordered. Returns a dataframe. This is
# # needed when the index gets shuffled due to merging two
# # dataframes or sorting a dataframe.



data=pd.read_csv("C:/code_fun/1_NUMPY/Screentime - App Details.csv", na_values=["08/27/2022","08/28/2022"])
# print(data.head())  #na_values=["08/27/2022","08/28/2022"]  yani in 2 values ko NaN consider
                        # krna h

data.columns=(data.columns.str.lower())  #yani sab columns ka name lower letter m ho gya
data.columns=data.columns.str.replace(" ","_") # ab times_opened esy ho gya or phly
                        # esy tha "times opened", this step is made to adopt snake_case format
print(data.columns)  
print(data.head())


