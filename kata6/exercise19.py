def narcissistic( value ):
    if value <10:
        return True
    else:
        val = 0
        for i in str(value):
            k = int(i)
            l = len(str(value))
            val +=pow(k,l)
        if val == value:
            return True
        else:return False
narcissistic(153)