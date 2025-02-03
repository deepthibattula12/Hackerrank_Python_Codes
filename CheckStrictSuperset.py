# Enter your code here. Read input from STDIN. Print output to STDOUT
n=set(map(int,input().split()))
n1=int(input())
n2=set(map(int,input().split()))
n3=set(map(int,input().split()))
n4=n.intersection(n2)
n5=n.intersection(n3)
if n4==n2 and n5==n3:
    print("True")
else:
    print("False")
