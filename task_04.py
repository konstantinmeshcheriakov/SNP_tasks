def sort_list(arr):
    arr1 = []
    if arr == []:
        return []
    for i in arr:
        if i == min(arr):
            arr1.append(max(arr))
        elif i == max(arr):
            arr1.append(min(arr))
        else:
            arr1.append(i)
    arr1.append(min(arr1))
    return arr1

