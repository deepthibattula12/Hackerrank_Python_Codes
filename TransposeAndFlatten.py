import numpy as np
n=input().split()
l=[]
for i in range(int(n[0])):
    k=list(map(int,input().split()))
    l.append(k)
a=np.array(l)
print(np.transpose(a))
print(a.flatten())
