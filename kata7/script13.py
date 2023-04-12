def xo(s):
    str = s.lower()

    x=0
    o=0
    for i in str:
        if i=='x':
            x +=1
        elif i == 'o':
            o+=1
    if x==o:
        return True
    else:
        return False

print(xo("oOxx"))