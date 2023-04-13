def multiples(num):
    arr = []
    while num>0:
        num -=1
        arr.append(num)
    arr1=[]
    for n in arr:
        if n % 3==0 and n % 5==0:
            arr1.append(n)  
        elif n % 3==0 and n % 5!=0:
            arr1.append(n)
        elif n % 5==0 and n % 3!=0:
            arr1.append(n)     
    print(arr1)
    print(sum(arr1))
multiples(6)