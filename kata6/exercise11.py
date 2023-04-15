def find_outlier(integers):
    odd = 0
    even=0
    for num in integers:
        if (num %2 !=0):
            odd +=1
        else:
            even+=1
    if odd > 1:
        for n in integers:
            if (n %2 ==0):
                return n
    elif even > 1:
        for n in integers:
            if (n %2 != 0):
                return n   

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))