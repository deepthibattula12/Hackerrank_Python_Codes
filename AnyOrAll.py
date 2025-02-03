n=int(input())
k=[]
h=[]
l=list(map(int,input().split()))
for i in l:
    if i>0:
        k.append(1)
    else:
        k.append(0)
def p(n):
    k=str(n)
    if k==k[::-1]:
        h.append(1)
    else:
        h.append(0)
if(all(k)):
    for i in l:
        p(i)
    print(any(h))
else:
    print("False")

