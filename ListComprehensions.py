if __name__ == '__main__':
    l=[]
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    r=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    for i in r:
        if(sum(i)!=n):
            l.append(i)
        else:
            continue
    print(l)
