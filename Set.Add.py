# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=set()
c=0
for i in range(n):
    s.add(input())
for i in s:
    c=c+1
print(c)
