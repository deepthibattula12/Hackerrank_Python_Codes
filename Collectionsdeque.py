from collections import deque
n=int(input())
d=deque()
for i in range(n):
    k=input().split()
    if k[0]=="append":
        d.append(int(k[1]))
    elif k[0]=="pop":
        d.pop()
    elif k[0]=="popleft":
        d.popleft()
    elif k[0]=="appendleft":
        d.appendleft(int(k[1]))
for i in d:
    print(i,end=' ')
    
