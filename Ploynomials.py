import numpy as np
l=list(map(float,input().split()))
n=int(input())
print(np.polyval(l,n))
