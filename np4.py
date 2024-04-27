import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr1)
print(arr1.shape)
print(arr1[0,2])  #1st row 3rd column
print(arr1[0],arr1[2])
print(arr1[:,0])  #1st column
print(arr1[-1,-1])
print(arr1[:,-1])   #last column
print(arr1[:,2])    #last column
print(arr1[-1])     #last row

print()
list1=[2,4,6,8,10]
print(list1[-1])
print(list1[-2])
