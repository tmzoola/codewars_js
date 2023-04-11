def filter_list(l):
    arr = []
    for i in l:
        if type(i) == int:
            arr.append(i)

    return arr

print(filter_list([1,2,'aasf','1','123',123]))