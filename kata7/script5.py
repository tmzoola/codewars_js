def high_and_low(numbers):
    arr = numbers.split(" ")
    arr2 = []
    for i in arr:
        arr2.append(int(i))
    arr3 = [str(max(arr2)), str(min(arr2))]
    return ' '.join(arr3)

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))