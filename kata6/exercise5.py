def spinWords(word):
    words = word.split(" ")
    arr=[]
    for i in words:
        if len(i)<=4:
            arr.append(i)
        elif(len(i)>4):
            arr.append(i[::-1])
    
    return ' '.join(arr)

spinWords("Hey fellow warriors")