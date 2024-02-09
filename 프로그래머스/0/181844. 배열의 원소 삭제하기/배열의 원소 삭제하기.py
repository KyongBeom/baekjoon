def solution(arr, del_lst):
    for i in del_lst:
        if i in arr:
            arr.pop(arr.index(i))
        else:
            pass
    return arr