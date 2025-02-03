import numpy as np
n=int(input())
l=[]
if n==3:
    for i in range(n*2):
        k=list(map(int,input().split()))
        l.append(k)
    a=np.array([l[0],l[1],l[2]])
    b=np.array([l[3],l[4],l[5]])
else:
    for i in range(n*2):
        k=list(map(int,input().split()))
        l.append(k)
    a=np.array([l[0],l[1]])
    b=np.array([l[2],l[3]])
print(np.dot(a,b))
