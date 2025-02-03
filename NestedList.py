if __name__ == '__main__':
    n=int(input())
    a=[]
    for i in range(n):
        k=input()
        k1=float(input())
        a.append([k,k1])
    l=[]
    h1=[]
    for i in range(0,len(a)):
        l.append(a[i][1])
    l.sort()
    k=set(l)
    h=sorted(list(k))
    o=h[1]
    for i in range(0,len(a)):
        if(o==a[i][1]):
            h1.append(a[i][0])
    h1.sort()
    for i in h1:
        print(i,end='\n')
