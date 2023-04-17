def dig_pow(n, p):
    res = 0
    m=p-1
    for i in str(n):
        l=int(i)
        m=m+1
        k = pow(l,m)
        res = res + k

    if res % n ==0:
        return res /n
    else: return -1

print(dig_pow(92, 1))