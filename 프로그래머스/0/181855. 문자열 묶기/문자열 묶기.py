def solution(arr):
    arr2 = [len(i) for i in arr]
    cnt = 0
    for i in set(arr2):
        if arr2.count(i) > cnt:
            cnt = arr2.count(i)
    return cnt