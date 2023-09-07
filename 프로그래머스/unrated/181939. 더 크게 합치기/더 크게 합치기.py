def solution(a, b):
    answer = 0
    check1 = str(a)+str(b)
    check2 = str(b)+str(a)
    if int(check1) > int(check2):
        return int(check1)
    else:
        return int(check2)