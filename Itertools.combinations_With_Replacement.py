# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
n=input().split()
k1=sorted(list(n[0]))
k=sorted(list(combinations_with_replacement(k1,int(n[1]))))
for i in k:
    print(''.join(i))
