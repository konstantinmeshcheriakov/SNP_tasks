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
    return dict(sorted(res.items(), key=lambda item: item[1]))
