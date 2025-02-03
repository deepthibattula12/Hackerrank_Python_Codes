def swap_case(s):
    l=[]
    for i in s:
        if(i.isupper()):
            l.append(i.lower())
        else:
            l.append(i.upper())
    return ''.join(l)

