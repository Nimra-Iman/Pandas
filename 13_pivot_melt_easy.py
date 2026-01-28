# # they are used for reshaping dataframes
import pandas as pd
df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
                           'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
# print(df)
# print(df.shape)  #(6, 4) yani df m 6 rows hn or 4 columns hn
# #-------> One way to reshape dataframes is to use pivot:
# # in pivot, one column is set as index, one column is set as column name and other
# # columns are used for representing actual dataset but you can use one column
# # as well.
new=pd.pivot(df, index="foo", columns="bar")
# # new=pd.pivot(df, index="foo", columns="bar", values="baz")  #esa krny s dataset m just 
#                                 # baz ki values show hon gi
# print(new)
# # THERE CANNOT BE A DUPLICATE VALUES IN INDEX IN PIVOT BUT PIVOT-TABLE CAN HAVE.

# print()
# print()
# # ----- pivot-table:   (is ka advantage y h k hm ek s ziada indexes de skty hn or
#                 # y achy s manage kr leta h)
n=df.pivot_table( index=["foo",'bar'], columns='zoo')
# print(n)
# print()
# print()
# print()

# # -----------  melt  ---------------------------------------------
# print(pd.melt(df, id_vars='foo', var_name="vaaarss" ))





#       ------------------------  EASYYYYYYYYYYYYYYYYY  ------------------------------
                                        # MELT
import pandas as pd
data = pd.read_csv('weather.csv')
# print(data)   #is table format pr analysis difficult h, we will format it usijg melt
d = pd.melt(data, id_vars = 'day' ) #id_vars m vo column rkhna h jis ko 
# hm chnage nhi krna chahty, ab melt to ho gya table but column ka name variable and value
# a rha h, us ko following way s chnage kryn gy
d = pd.melt(data, id_vars = 'day', var_name = 'city', value_name='temperature') # out data is
# finally ready and we can apply filters to show the temperature of specific city, like below
# print(d[d['city']=='chicago'])
# print(d)


                                    # PIVOT
# both pivot and pivot table are used for reshaping the dataframe to make it better for 
# visualisation, the difference beteween pivot and pivot table is that pivot cannot take
# duplicate values and we cannot apply aggregate functions to column s by using pivot, but
# both these things is possible in pivot table.

# in both pivot and pivot table, one column is set as index (which will be shown in 
# x-axis while visualising) and one column is set as columns, jo k sab s uper horizontally
# show ho ga and in dono ki base pr andr values fill ki jayn gi

data = pd.read_csv('weather2.csv')
# print(data)

# p = pd.pivot(data, index = 'date', columns = 'city')
# print(p)   This will give error because because row index 4 and 5 m date and city same h
# and we already said that pivot m duplicate values na ho
# p = pd.pivot(data, index = 'date', columns = 'humidity')
# print(p) #  vo columns jo hm index and columns m pass kr rhy hn un m duplicated entries 
# ho gi to hi pivot error show kry ga, agr index and columns m na ho or baki dataet m ho
# to pivot bhi error show nhi kry ga

# FOR THIS REASON, WE WILL USE PIVOT TABLE FOR THIS DATASET:
pt = pd.pivot_table(data, index = 'date', columns = 'city')
print(pt)   #is n aggregated function apply kr k result show kia and 'aggfunc' m mean is
# by default function, q k pury dataset m ek date and ek city pr 2 2 humidity and temperature
# ki values thi, us n dono values ka mean lia or show kr dia,,, we can also chnage 
# aggfunc as count, add etc etc 

# pt = pd.pivot_table(data, index = 'date', columns = 'temperature')
# print(pt) error because agg function failed [how->mean,dtype->object]

pt = pd.pivot_table(data, index = 'date', columns = 'city', margins=True)
print(pt) 
