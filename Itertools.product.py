# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
k=input().split()
k1=input().split()
l=list(map(int,k))
l1=list(map(int,k1))
k2=list(product(l,l1))
for i in k2:
    print(i,end=' ')
