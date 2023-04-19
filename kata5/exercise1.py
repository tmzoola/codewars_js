def move_zeros(lst):
    arr1 =[]
    arr2=[]
    for i in lst:
        if i == 0:
            arr1.append(i)
        else:
            arr2.append(i)
    for a in arr1:
        arr2.append(a)
    
    return arr2

move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])