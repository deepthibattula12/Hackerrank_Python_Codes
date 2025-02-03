if __name__ == '__main__':
    n = int(input())
    k={}
    for i in range(n):
        d=input().split(' ')
        n1=d[0]
        s=list(map(float,d[1:]))
        k[n1]=s
    name=input()
    if name in k:
        a=sum(k[name])/len(k[name])
        print("%.2f"%a)
