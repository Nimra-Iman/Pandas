import pandas as pd
df = pd.DataFrame({
    "Name": ["Ali", "Sara"],
    "Math": [90, 85],
    "Science": [88, 95]
})

d = pd.melt(df,id_vars='Name', value_name= 'subject',var_name='marks')
print(d)

 

