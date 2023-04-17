
def find_uniq(arr):
    x = set(arr)
    for i in x:
        a= arr.count(i)
        if a==1:
            return i
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))