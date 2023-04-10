#Your task is to make a function that can take any non-negative integer as an argument
#and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

#Examples:
#Input: 42145 Output: 54421

#Input: 145263 Output: 654321


def descending_order(num):
    arr = []
    for i in str(num):
        arr.append(int(i))
    a=[]
    while arr != []:
        for k in arr:
            if k == max(arr):
                a.append(str(k))
                arr.remove(k)

    return int(''.join(a))  

        
    
descending_order(42145)