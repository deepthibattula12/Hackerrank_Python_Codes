import numpy as np
n=input().split()
l=[]
for i in range(int(n[0])):
    n1=list(map(int,input().split()))
    l.append(n1)
a=np.array(l)
print(np.mean(a,axis=1))
print(np.var(a,axis=0))
print(round(np.std(a),11))
