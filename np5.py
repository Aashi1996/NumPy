import numpy as np

arr1=np.ones([3,3])
arr2=np.full([3,3],4)
print(arr1)
print(arr2)

arr3=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr3.reshape([6,2]))
print(arr3.reshape([3,4]))
print(arr3.T)

arr4=np.random.random((3,4))
print(arr4)

arr5=np.random.randint(9,size=10)
print(arr5)

arr6=np.random.randint(99,size=(4,3))
print(arr6)
