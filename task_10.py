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
        return dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))



