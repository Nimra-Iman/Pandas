import pandas as pd

data = pd.read_csv('weather2.csv')
# print(data)

# p = pd.pivot(data, index = 'date', columns = 'city')
# print(p)   #This will give error because because row index 4 and 5 m date and city same h
# and we already said that pivot m duplicate values na ho
# p = pd.pivot(data, index = 'date', columns = 'humidity')
# print(p) #  vo columns jo hm index and columns m pass kr rhy hn un m duplicated entries 
# ho gi to hi pivot error show kry ga, agr index and columns m na ho or baki dataet m ho
# to pivot bhi error show nhi kry ga

# FOR THIS REASON, WE WILL USE PIVOT TABLE FOR THIS DATASET:
# pt = pd.pivot_table(data, index = 'date', columns = 'city')
# print(pt)   #is n aggregated function apply kr k result show kia and 'aggfunc' m mean is
# # by default function, q k pury dataset m ek date and ek city pr 2 2 humidity and temperature
# # ki values thi, us n dono values ka mean lia or show kr dia,,, we can also chnage 
# # aggfunc as count, add etc etc 
# pt = pd.pivot_table(data, index = 'date', columns = 'city', aggfunc='count')
# print(pt)   #here aggfunc is count

# pt = pd.pivot_table(data, index = 'date', columns = 'temperature')
# print(pt) # error because agg function failed [how->mean,dtype->object]

