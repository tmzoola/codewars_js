def order(sentence):
    sen = sentence.split(' ')
    num =0
    arr=[]
    while num <10:
        num+=1
        for word in sen:
            if str(num) in word:
                arr.append(word)
    
    return ' '.join(arr)
                
        


order("is2 Thi1s T4est 3a")