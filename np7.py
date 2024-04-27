import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
sum_allrows = arr1.sum()
sum_rows1 = arr1.sum(axis=1)[0]
#sum_rows12 = arr1.sum(axis=1)[0,1]
sum_rows123 = arr1.sum(axis=1)
sum_cols1 = arr1.sum(axis=0)[0]
#sum_cols12 = arr1.sum(axis=0)[0,1]
sum_cols123 = arr1.sum(axis=0)
print(sum_allrows)
print(sum_rows1)
print(sum_cols1)
max_all = arr1.max()
max_rows1 = arr1.max(axis=1)[0]
#max_rows12 = arr1.max(axis=1)[0,1]
max_rows123 = arr1.max(1)
print(max_all)
print(max_rows1)
min_all = arr1.min()
print(min_all)
