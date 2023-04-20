def pig_it(text):
    txt = text.split(' ')
    arr = []
    for i in txt:
        if (i.isalpha()):
            arr.append(i[1:]+ i[0] + 'ay')
        else:
            arr.append(i)
    return ' '.join(arr)
pig_it('This is my string')