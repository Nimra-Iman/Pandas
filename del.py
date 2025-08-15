import pandas as pd
<<<<<<< HEAD
df = pd.DataFrame({
    "Name": ["Ali", "Sara"],
    "Math": [90, 85],
    "Science": [88, 95]
})

d = pd.melt(df,id_vars='Name', value_name= 'subject',var_name='marks')
print(d)

 

=======
data = pd.read_csv('C:\\code_fun\\1_NUMPY\\Screentime - App Details.csv')


# print(data.head)
data = data.sort_values(by = 'Notifications', ascending=True)

data = data.reset_index(drop=True)
print(data.head)
>>>>>>> ff645e9 (add more files)
