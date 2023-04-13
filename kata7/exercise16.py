def DNA_strand(dna):
    arr=[]
    for i in dna:
        if i == "A":
            arr.append("T")
        elif i == "T":
            arr.append("A")
        elif i == "C":
            arr.append("G")
        elif i == "G":
            arr.append("C")
    return ''.join(arr)

DNA_strand("ATTGC")