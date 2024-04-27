import numpy as np
import pandas as pd
info=pd.read_csv("im4.csv")
print(info)
print(info.iloc[0,1])
info1=info.query('Rank==1')
print(info1.iloc[:,1])
