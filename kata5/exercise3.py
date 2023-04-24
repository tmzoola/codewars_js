def generate_hashtag(s):
    hashtag = s.split(' ')
    arr=[]
    if s == "" or len(s)>=140:
        return False
    
    else:
        for i in hashtag:
            if i != "" or len(i)<=140:
                arr.append(i.capitalize())

        return "#" + ''.join(arr)
        
print(generate_hashtag("Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat"))