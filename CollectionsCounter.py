# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
k=list(map(int,input().split()))
n1=int(input())
s=0
for i in range(n1):
    k1=list(map(int,input().split()))
    if k1[0] in k:
        s=s+k1[1]
        k.remove(k1[0])
    else:
        continue
print(s)

