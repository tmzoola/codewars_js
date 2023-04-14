def root(number):
    sum = 0
    for num in str(number):
        sum = sum + int(num) 
    if len(str(sum))==1:
        return sum
    else:
        value = root(sum)
        return value
print(root(493193))