import pandas as pd
import numpy as np

data=pd.read_csv("my_file1.csv")
new_data=data.fillna(method="bfill", axis=1)
print(new_data)

