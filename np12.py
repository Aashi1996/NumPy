import numpy as np
info=np.loadtxt("im4.csv",delimiter="\n",dtype=str)
print(info)
print()
info1=np.genfromtxt("im4.csv",delimiter="\n",dtype=str)
print(info1)
