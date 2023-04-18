def solution(s):
    n=2
    arr = []
    for i in range(0,len(s),n):
        arr.append(s[i:i+n])
    
    for k in arr:
        if len(k)==1:
            arr[len(arr)-1]=k+'_'
    return arr

solution('abcde')