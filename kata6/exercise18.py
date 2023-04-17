def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    elif len(sequence)==1:
        for i in sequence: return [i]
    else:
        arr=[]
        for i in sequence:
            if len(arr) < 1 or not i == arr[len(arr) - 1]:
                arr.append(i)
        return arr


print(unique_in_order(("ABBCcA")))