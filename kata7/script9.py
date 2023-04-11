import math

def is_square(n):
    if n == -1:
        return False
    elif n<0:
        n= -n
        a = math.sqrt(n)
        if a**2 == n:
            return True
        else:
            return False  
    
    else:
        a = math.sqrt(n)
        if a**2 == n:
            return True
        else:
            return False

print(is_square(-1))