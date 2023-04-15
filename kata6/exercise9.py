def array_diff(a, b):
    if a == []:
        return a
    elif b == []:
        return a
    elif b != [] and a != []:
        for d in b:
            while d in a:
                a.remove(d)
        
        return a 

    print(a,b)

array_diff([1,2,2], [2])