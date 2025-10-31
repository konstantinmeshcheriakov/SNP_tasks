def coincidence(ls = [], ran = range(0)):
    arr = []
    if ls == [] or ran == range(0):
        return []
    for i in range(len(ls)):#выбор числовых значений из исходного списка
        if type(ls[i]) == int or type(ls[i]) == float:
            if ls[i] >= min(ran) and ls[i] <= max(ran):
                arr.append(ls[i])
            else:
                continue            
        else:
            continue
    return arr  


