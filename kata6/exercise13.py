def alphabet_position(text):
    a = 'abcdefghijklmnopqrstuvwxyz'

    arr = []
    for i in text:
        if a.find(i.lower())+1 >0:
            arr.append(str(a.find(i.lower())+1))


    return ' '.join(arr)

alphabet_position("The sunset sets at twelve o' clock.")