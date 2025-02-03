if __name__ == '__main__':
    N = int(input())
    l=[]
    for _ in range(N):
        i=input().split()
        if(i[0]=='insert'):
            l.insert(int(i[1]),int(i[2]))
        elif(i[0]=='print'):
            print(l)
        elif(i[0]=='remove'):
            l.remove(int(i[1]))
        elif(i[0]=='sort'):
            l.sort()
        elif(i[0]=='reverse'):
            l.reverse()
        elif(i[0]=='pop'):
            l.pop()
        elif(i[0]=='append'):
            l.append(int(i[1]))
            
        
