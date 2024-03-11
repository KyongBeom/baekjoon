def solution(s):
    s = s.lower()
    check1 = 0
    check2 = 0
    for i in s:
        if i == "p":
            check1 += 1
        elif i == "y":
            check2 += 1
    if check1 == check2:
        return True
    else:
        return False