def to_camel_case(text):
    if text == "":
        return ""
    for i in text:
        if i == "-" or i =="_":
            a = text.replace(i, " ")
    print(a)
    arr = []
    for k in a.split(' '):
        if k == a.split(' ')[0]:
            arr.append(k)
        else:
            arr.append(k.capitalize())
    
    return ''.join(arr)
        

print(to_camel_case("A_Cat-Is-kawaii"))