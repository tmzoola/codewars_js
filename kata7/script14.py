def to_jaden_case(string):
    arr = string.split(' ')
    arr2 = []
    for i in arr:
        n = i.capitalize()
        arr2.append(n)
    return ' '.join(arr2)
to_jaden_case("How can mirrors be real if our eyes aren't real")