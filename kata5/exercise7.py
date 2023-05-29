def scramble(s1, s2):
    common_chars = [char for char in s1 if char in s2]

    for char in common_chars:
        s1 = s1.replace(char, "")
        s2 = s2.replace(char, "")
    if s2 == "":
        return True
    else:
        return False
scramble('ciqvsuhinkgg', 'ivvigshk')