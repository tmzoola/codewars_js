def first_non_repeating_letter(string):
    var = ""
    for i in string.lower():
        if(string.lower().count(i)==1):
            var = i
            break
    if var in string:
        return var
    else:
        return var.upper()

first_non_repeating_letter('sTreSS')