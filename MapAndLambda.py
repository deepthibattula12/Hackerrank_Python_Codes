cube = lambda x: x**3
def fibonacci(n):
    # return a list of fibonacci numbers
    k=n
    n1=0
    n2=1
    l=[0,1]
    while(n!=0):
        n3=n1+n2
        l.append(n3)
        n1=n2
        n2=n3
        n=n-1
    return l[:k]

