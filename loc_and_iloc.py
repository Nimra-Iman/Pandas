# -----------------------  loc  -----------------------------
# The loc() function is label based data selecting method which means that we have to 
# pass the name of the row or column which we want to select.
import pandas as pd
x={"name":["pop","bob","joe"],"age":[21,23,21],"edu":["BA","MA","BA"]}
data=pd.DataFrame(x)
print(data)

#        1-   Selecting Data According to Some Conditions:
print(data.loc[(data["age"]==21) & (data["edu"]=="BA")])


#        2: Selecting a Range of Rows From the DataFrame
print(data[1:3])


#       3: Updating the Value of Any Column
print()
data.loc[1, "age"]= 24
print(data)

#       4: Select a specific range of data
print()
