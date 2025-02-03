import numpy as np
l=[]
for i in range(2):
    k=list(map(int,input().split()))
    l.append(k)
a=np.array(l[0])
b=np.array(l[1])
print(np.inner(a,b))
print(np.outer(a,b))
