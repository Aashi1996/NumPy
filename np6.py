import numpy as np

arr6=np.random.randint(9,size=(4,3))
print(arr6)
print(arr6.sum())
print(arr6.sum(axis=1))     #sum of each row is shown
print(arr6.sum(axis=1)[0])  #sum of first row
print(arr6.sum(axis=0))     #sum of each column is shown

