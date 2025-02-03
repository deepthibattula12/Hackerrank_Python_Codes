import numpy as np
n=input().split()
l=[]
for i in range(int(n[0])):
    n1=list(map(int,input().split()))
    l.append(n1)
a=np.sum(l,axis=0)
print(np.prod(a))
