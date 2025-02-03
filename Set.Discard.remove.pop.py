n=int(input())
s=set(map(int,input().split()))
k=int(input())
for i in range(1,k+1):
    k1=input().split()
    if k1[0]=='pop':
        s.pop()
    elif k1[0]=='remove':
        s.remove(int(k1[1]))
    elif k1[0]=='discard':
        s.discard(int(k1[1]))
    else:
        print("No such operation")
    
print(sum(s))
