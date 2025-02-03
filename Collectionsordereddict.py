from collections import OrderedDict
d=OrderedDict()
n=int(input())
for i in range(n):
    k=input()
    *item,amt=k.rsplit(' ',1)
    item=' '.join(item)
    amt=int(amt)
    if item in d:
        d[item]+=amt
    else:
        d[item]=amt
for i,j in d.items():
    print(i,j)
               
               
