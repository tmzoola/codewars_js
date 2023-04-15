def duplicate_encode(word):
    arr = []
    for i in word.lower():
        if word.lower().count(i)>1:
            arr.append(")")
        else:
            arr.append("(")
    return ''.join(arr)
duplicate_encode("(( @")