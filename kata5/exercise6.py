def increment_string(strng):
    a = strng.rstrip('0123456789')

    b = strng[len(a):]

    if len(b) != 0:
        c= str(int(b)+1)
        if len(b)>len(c):
            return a +((len(b)-len(c))*"0")+c
        else:
            return a +c      
    else:
        return strng + "1"

            


print(increment_string("foo"))