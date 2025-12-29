# Написать метод multiply_numbers(inputs), который вернет произведение цифр,
# входящих в inputs.
# Тест для примеров и проверки:
# multiply_numbers() # => None
# multiply_numbers('ss') # => None
# multiply_numbers('1234') # => 24
# multiply_numbers('sssdd34') # => 12
# multiply_numbers(2.3) # => 6
# multiply_numbers([5, 6, 4]) # => 120
def proverka(a):
    n = '1234567890'
    arr = []
    for i in a:
        if str(i) in n:
            arr.append(i)
        if len(arr) != 0:
            res = 1
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
        list(a)
        return proverka(a)
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

print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120