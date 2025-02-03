if __name__ == '__main__':
    n=int(input())
    i=input().split()
    l=[int(x) for x in i]
    s=set(l)
    l1=list(s)
    l1.sort()
    print(l1[len(l1)-2])
