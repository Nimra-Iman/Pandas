import pandas as pd

import pandas as pd
data = pd.read_csv('weather2.csv')
print(data)   #is table format pr analysis difficult h, we will format it usijg melt
# d = pd.melt(data, id_vars = 'day' ) #id_vars m vo column rkhna h jis ko 
# # hm chnage nhi krna chahty, ab melt to ho gya table but column ka name variable and value
# # a rha h, us ko following way s chnage kryn gy
# d = pd.melt(data, id_vars = 'day', var_name = 'city', value_name='temperature') # out data is
# # finally ready and we can apply filters to show the temperature of specific city, like below
# # print(d[d['city']=='chicago'])
# # print(d)



