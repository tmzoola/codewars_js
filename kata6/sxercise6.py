def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i


find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])