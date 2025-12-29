# Анаграмма — литературный приём, состоящий в перестановке букв или звуков
# определённого слова (или словосочетания), что в результате даёт другое слово
# или словосочетание.
# Разработайте метод combine_anagrams(words_array), который принимает на вход
# массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
# значения при определении анаграмм.
# Тест для примеров и проверки:
# combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
# "creams", "scream"]) # => [ ["cars", "racs", "scar"], ["four"], ["for"],
# ["potatoes"], ["creams", "scream"] ]

def combine_anagrams(arr):
    word = ''
    arr1 = []
    res = []
    res1 = []
    for i in arr:
        word = list(i.lower())
        for i in range(0, len(arr)):
            if sorted(word) == sorted(list(arr[i].lower())):
               arr1.append(arr[i])
            else:
                continue
        res.append(arr1)
        arr1 = []
    for i in res:
        if i not in res1:
            res1.append(i)
    return res1
print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
# => [ ["cars", "racs", "scar"], ["four"], ["for"],["potatoes"], ["creams", "scream"] ]