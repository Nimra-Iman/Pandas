import pandas as pd
# -------------  DataFrames ----------------
# via dict, via list of list, via series

# x={"a":["wd","we"],"b":["fd","gt"],"c":["fe","re"]}
# x=[[1,2,3],[6,7,8]]
x={"a":pd.Series(["wd","we"]), "b":pd.Series(["fd","gt"])}

data=pd.DataFrame(x)
print(data)

