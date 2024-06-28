import pandas as pd
data = pd.DataFrame({
    "name": ["Alice", "Bob", "Alice", "Bob", "Alice", "Alice", "Alice", "Bob", "Bob"],
    "age": [25, 30, 35, 40, 67, 43, 21, 34, 65],
    "number": [56, 78, 45, 67, 98, 65, 43, 21, 21]
})


data1=data.groupby("name")
# for name,data in data1:
#     print(name)
#     print(data)
#     print()


print(data1.get_group("Bob"))
print(data1.max())








# # import doctest
# # def square(x):
# #     '''This function will take value of x as an argument and then
# #         return return the square of x'''
# #     return x*2
# # print(square(2))

# # if __name__ == "__main__":
# #     doctest.testmod()


# import doctest

# def square(x):
#     '''
#     This function computes the anti-log of a number.
    
#     '''
#     return x ** 2

# # Running doctests
# if __name__ == "__main__":
#     doctest.testmod()
# print(square(2))










# # ASK FROM CHATGPT 4.o
# # in this dataset:  Unnamed: 0     Brand    Year  Kms Driven     City  Mileage
# # 0         0.0    Maruti  2012.0     50000.0      NaN     28.0
# # 1         1.0       NaN  2014.0         NaN    Delhi     27.0
# # 2         2.0      Tata  2011.0         NaN   Mumbai     25.0
# # 3         3.0  Mahindra  2015.0         NaN    Delhi     26.0
# # 4         4.0    Maruti     NaN     10000.0   Mumbai     28.0
# # 5         5.0   Hyundai  2016.0     46000.0    Delhi     29.0
# # 6         6.0   Renault  2014.0     31000.0   Mumbai     24.0
# # 7         NaN       NaN     NaN         NaN      NaN      NaN
# # 8         7.0      Tata  2018.0     15000.0  Chennai     21.0
# # 9         8.0    Maruti  2019.0     12000.0      NaN     24.0    the above dataset that i showed you, you said that limit_area="inside" will fill only those NaN that are bounded by non-NA values, Now, in BRAND, on row no 1,2,3 , why they are filled on passing limit_area="inside":print(data.interpolate(axis=0, limit=2, limit_area="inside"))  #default= axis=0(column)