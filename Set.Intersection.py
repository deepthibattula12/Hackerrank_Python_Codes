# Enter your code here. Read input from STDIN. Print output to STDOUT
c=0
n=int(input())
k=input().split()
h=set(map(int,k))
n1=int(input())
k1=input().split()
h1=set(map(int,k1))
s=h.intersection(h1)
for i in s:
    c=c+1
print(c)

