def max_odd(arr):
    arr1 = []
    value = 0
    for i in range(len(arr)):
        if type(arr[i]) == int or type(arr[i]) == float:
            if arr[i] % 2 != 0 and arr[i] > value:
                value = arr[i]
            else:
                continue
        else:
            continue
    if value == 0:
        return None
    else:
        return value



