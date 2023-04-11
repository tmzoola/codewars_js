
#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    arr = []
    k=1
    for i in s:
        a = i*k
        arr.append(a.capitalize())
        k=k+1
    b= (arr)
    return '-'.join(b)
    
print(accum("ZpglnRxqenU"))