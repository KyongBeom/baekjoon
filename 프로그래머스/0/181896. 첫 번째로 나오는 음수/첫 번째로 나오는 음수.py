def solution(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            return i
    return -1
