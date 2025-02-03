# Enter your code here. Read input from STDIN. Print output to STDOUT
l=input().split()
p=list(map(int,l[0:]))
k=input()
n=k.replace('x',str(p[0]))
k1=eval(n)
if(k1==p[1]):
    print("True")
else:
    print("False")
