import numpy as np
n=list(map(int,input().split()))
p=n[0]+n[1]
l=[]
for i in range(p):
    k=list(map(int,input().split()))
    l.append(k)
a=np.array(l)
print(a)
