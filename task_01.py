def is_palindrom(s):
    p = ",.'-:;!?"
    if s == None:
        return False
    elif type(s) != str and s != None:
        s = str(s)
        s = s.replace('--', '')
        s = s.replace(' ', '')
        s = list(s.lower())
    elif type(s) == str and s != None:
        s = s.replace('--', '')
        s = s.replace(' ', '')
        s = list(s.lower())
    for i in s:
        if i in p:
            s.remove(i)
        else:
            continue
    if s == s[::-1]:
        return True
    else:
        return False




    