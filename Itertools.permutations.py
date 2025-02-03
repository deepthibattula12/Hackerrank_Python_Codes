# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
k=input().split()
l=list(map(str,k[0]))
k1=sorted(list(permutations(l,int(k[1]))))
for i in k1:
    print(''.join(i))
