def maskify(word):
    if len(word)>4:
        arr = []
        word1 = word[:-4]
        for i in word1:
            arr.append("#")
        arr.append(word[-4:])
        
        return''.join(arr)
    else:
        return word            
    

maskify("4556364607935616")