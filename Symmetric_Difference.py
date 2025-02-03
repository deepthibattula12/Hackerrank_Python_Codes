# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
k=set(map(int,input().split()))
n1=int(input())
l=set(map(int,input().split()))
k1=k.intersection(l)
k2=k.union(l)
k3=k2.difference(k1)
b=sorted(list(k3))
for i in b:
    print(i,end='\n')
