import numpy as np 
info=np.genfromtxt("im4.csv",delimiter=",",dtype=str)
print(info)
print(info[1,1])
info1=np.genfromtxt("im4.csv",delimiter=",",dtype=int)
print(info1)
