def proverka(a):
    n = '1234567890'
    arr = []
    res = 1
    for i in a:
        if str(i) in n:
            arr.append(i)
    if len(arr) != 0:
        for i in arr:
            res = res * int(i)
        return res
    else:
        return None
def multiply_numbers(a = None):
    #проверка на вводимые значения
    arr = []
    if a == None:
        return None
    elif type(a) == str:
        res = proverka(a)
        return res
    elif type(a) == float:
        s = list(str(a))
        s.remove('.')
        res = 1
        for i in s:
            res = res * int(i)
        return res
    elif type(a) == list:
        return proverka(a)
    else:
        return a

