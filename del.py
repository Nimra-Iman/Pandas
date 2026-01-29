import pandas as pd
import numpy as np
data = pd.Series([1,2,3,4,5], index=[1,2,3,4,5], name = 'sereies')
print(data)
print((data.to_numpy()).dtype[0])



