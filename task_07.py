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