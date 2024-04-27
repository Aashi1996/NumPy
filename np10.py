import numpy as np

arr1=np.array([1,2,3,4,5,6,7,8,9])
print(arr1)
arr2=[]
for i in range(0,9,1):
    
    e1=arr1[i]
    r1=e1%2
    if r1!=0:
        arr2.append(0)
    else:
        arr2.append(e1)
print(arr2)


#[0,2,0,4,0,6,0,8,0]
