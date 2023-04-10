#Your task is to write a function that takes a string and return a new string with all vowels removed.

#For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

#Note: for this kata y isn't considered a vowel.


def disemvowel(string_):
    arr = []
    for i in string_:
        if i!="a" and i!="o" and i!="u" and i!="i" and  i!="e" and i!="A" and i!="O" and i!="U" and i!="I" and  i!="E" :
            arr.append(i)
        
    return ''.join(arr)
print(disemvowel("This website is for losers LOL!"))