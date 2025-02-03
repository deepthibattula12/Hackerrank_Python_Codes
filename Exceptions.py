k=int(input())
l=[]
for i in range(k):
    n=input().split()
    l.append(n)
for j in l:
    try:
        a=int(j[0])//int(j[1])
        print(a)
    except (ZeroDivisionError,ValueError) as e:
        print("Error Code:",e)

