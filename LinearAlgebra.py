import numpy as np
l=[]
n=int(input())
if n==3:
    for i in range(n):
        k=list(map(float,input().split()))
        l.append(k)
    a=np.linalg.det([l[0],l[1],l[2]])
else:
    for i in range(n):
        k=list(map(float,input().split()))
        l.append(k)
    a=np.linalg.det([l[0],l[1]])
print(round(a,2))
