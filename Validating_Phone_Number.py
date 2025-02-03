# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[]
for i in range(n):
    k=input()
    l.append(k)
for j in l:
    if len(j)==10 and j[0][0] in ['7','8','9'] and j.isdigit():
        print("YES")
    else:
        print("NO")

