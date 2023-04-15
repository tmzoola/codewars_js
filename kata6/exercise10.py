def create_phone_number(n):
    arr = []
    for i in n:
        arr.append(str(i))
    return "(" + ''.join(arr[0:3]) +")" + " "+ ''.join(arr[3:6]) + "-"+''.join(arr[6:10])

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])