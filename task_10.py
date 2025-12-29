# Разработайте функцию count_words(string), которая будет возвращать словарь со
# статистикой частоты употребления входящих в неё слов.
# Тесты для примеров и проверки:
# count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1,
# "canal": 1, "panama": 1, "plan": 1}
# count_words("Doo bee doo bee doo") # => {"doo": 3, "bee": 2}

# При выполнении следующих упражнений помните, что при получении невалидных
# параметров, в том числе неправильных типов данных, код программы не должен
# ломаться и должен выдавать всегда какое-либо значение. Название классов и их
# методы должны соответствовать тем, которые представлены в описании задачи.
def count_words(s, pr = None):
    if type(s) != str:
        print('Вводимое значнение должно быть строкой')
    elif pr != None:
        print('Должен передаваться всего один аргумент')
    else:
        pr = ",.'-=!/|?"
        arr = list(s)
        arr1 = []
        dict1 = {}
        counter = 0
        for i in arr:
            if i in pr:
                continue
            else:
                arr1.append(i)
        arr1 = "".join(arr1).lower().split()
        for i in range(0, len(arr1)):
            counter = arr1.count(arr1[i])
            dict1[arr1[i]] = counter
        print(dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True)))

count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
count_words("Doo bee doo bee doo") # => {"doo": 3, "bee": 2}
count_words(1)
count_words('d', '')

