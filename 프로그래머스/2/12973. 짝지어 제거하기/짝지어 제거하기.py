def solution(s):
    answer = -1
    check = []
    for i in s:
        if check and check[-1] == i:
            check.pop()
        else:
            check.append(i)
    if check:
        return 0
    else:
        return 1