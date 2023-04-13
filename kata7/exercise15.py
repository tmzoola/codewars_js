def find_short(s):
    arr = []
    for i in s.split(' '):
        arr.append(len(i))
    print( str(min(arr)))



find_short("bitcoin take over the world maybe who knows perhaps")