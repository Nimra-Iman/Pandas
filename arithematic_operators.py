import pandas as pd
x={"a":[20,21,23,45],"b":[45,32,12,45]}
data=pd.DataFrame(x)
print(data)


# -----------  ADD a and b:
data["sum"]=data["a"] + data["b"]  #ib "data" m ek new column add ho ga "sum" k name s jo
        # k a+b k equal ho ga
print(data)



# -----------  sub a and b:
data["sub"]=data["a"] - data["b"]  #ib "data" m ek new column add ho ga "sum" k name s jo
        # k a-b k equal ho ga
print(data)

# similarly , you can perform * and / too.


# ---------------  other logical operations:
data["comparison"]= data["a"]>=30   #
print(data)