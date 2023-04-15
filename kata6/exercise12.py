def duplicate_count(text):
    arr=[]
    for i in text:
         arr.append(i.lower())
    arr2=[]
    for i in arr:
         if arr.count(i)>1:
            arr2.append(i)   
    return len(set(arr2))
print(duplicate_count("ABBA"))