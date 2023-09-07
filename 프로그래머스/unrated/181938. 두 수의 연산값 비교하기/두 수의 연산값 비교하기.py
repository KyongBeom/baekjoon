def solution(a, b):
    check1 = str(a) + str(b)
    check2 = 2*a*b
    if int(check1) > check2:
        return int(check1)
    else:
        return check2
