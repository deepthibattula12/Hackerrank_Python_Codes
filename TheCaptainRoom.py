# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=list(map(int,input().split()))
d={}
for i in s:
    if i in d:
        d[i] +=1
    else:
        d[i]=1
for key in d.keys():
    if(d[key]==1):
        print(key)
        break
