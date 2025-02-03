# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    string=input()
    if string.isalnum() and len(string)==10:
        c1=0
        c2=0
        c3=0
        l=['1','2','3','4','5','6','7','8','9','0']
        for j in string:
            if j in l:
                c1=c1+1 #digits
        for j in string:
            if j.isupper():
                c2=c2+1 #upper?
        for j in string:
            if string.count(j)>1:
                c3=1 #duplicates
                break
        
        if c1>=3 and c2>=2 and c3!=1:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")    
