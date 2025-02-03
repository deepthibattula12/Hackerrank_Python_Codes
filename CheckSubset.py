# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[]
for i in range(n):
    n1=int(input())
    n2=set(map(int,input().split()))
    n3=int(input())
    n4=set(map(int,input().split()))
    n5=n2.intersection(n4)
    if n2==n5:
        l.append("True")
    else:
        l.append("False")
for i in l:
    print(i,end='\n')
