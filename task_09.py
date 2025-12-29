# Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
# переданных словаря, значениями ключей в которых являются числа, и вернет
# новый словарь, полученный по следующим правилам:

# • приоритетными являются ключи того словаря, сумма значений ключей
# которого больше (если суммы значений ключей будут равны, то второй
# словарь считается более приоритетным)
# • ключи со значениями меньше 10 не должны попасть в финальный
# словарь
# • получившийся словарь должен вернуться упорядоченным по значениям
# ключей в порядке возрастания.

# Тесты для примеров и проверки:
# connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) # =>
# { "c": 11, "b": 12 }
# connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # =>
# { d: 11, "c": 12, "a": 13 }
# connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) # =>
# { "c": 11, "b": 12, "a": 15 }
def connect_dicts(dict1, dict2):
    v_dict1 = 0
    v_dict2 = 0
    pr = 1
    dict11 = {}
    dict21 = {}
    res = {}
    for i in dict1:
        v_dict1 = v_dict1 + dict1[i]
    for i in dict2:
        v_dict2 = v_dict2 + dict2[i]
    if v_dict1 > v_dict2:
        pr = 1
    else:
        pr = 2
    for i in dict1:
        if dict1[i] < 10:
            continue
        else:
            dict11[i] = dict1[i]
    for i in dict2:
        if dict2[i] < 10:
            continue
        else:
            dict21[i] = dict2[i]
    for i in dict11:
        if i in dict21:
            if pr == 1:
                res[i] = dict11[i]
            else:
                res[i] = dict21[i]
        else:
            res[i] = dict11[i]

    for i in dict21:
        if i in dict11:
            if pr == 1:
                res[i] = dict11[i]
            else:
                res[i] = dict21[i]
        else:
            res[i] = dict21[i]           
    print(dict(sorted(res.items(), key=lambda item: item[1])))

connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) # => { "c": 11, "b": 12 }
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # => { d: 11, "c": 12, "a": 13 }
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) # => { "c": 11, "b": 12, "a": 15 }
