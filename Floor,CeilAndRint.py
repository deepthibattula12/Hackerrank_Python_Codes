import numpy as np
np.set_printoptions(legacy='1.13')
l=list(map(float,input().split()))
a=np.array(l)
np.set_printoptions(suppress=True)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))
