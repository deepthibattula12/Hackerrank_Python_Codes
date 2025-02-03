# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input().split()
l1=[]
for i in range(int(n[1])):
    k=input().split()
    l=list(map(float,k))
    l1.append(l)
k1=zip(*l1)
p=list(k1)
for i in p:
    print(sum(i)/len(i))
