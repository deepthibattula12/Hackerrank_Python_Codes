from collections import namedtuple
n=int(input())
s=[]
k=input().split()
p=namedtuple('p',k)
for i in range(n):
    k1=input().split()
    s1=p(k1[0],k1[1],k1[2],k1[3])
    s.append(s1)
Sum=0
c=0
for i in s:
    Sum=Sum+int(i.MARKS)
    c=c+1
print("%.2f"%(Sum/c))
