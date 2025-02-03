import numpy as np
n=input().split()
l=[]
if int(n[0])==1:
    for i in range(2):
        k=list(map(int,input().split()))
        l.append(k)
    a=np.array([l[0]])
    b=np.array([l[1]])
else:
    for i in range(int(n[1])):
        k=list(map(int,input().split()))
        l.append(k)
    a=np.array([l[0],l[1]])
    b=np.array([l[2],l[3]])
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.floor_divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))
