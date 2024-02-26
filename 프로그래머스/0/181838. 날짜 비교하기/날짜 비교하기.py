def solution(d1, d2):
    ans1 = int("".join(map(str,d1)))
    ans2 = int("".join(map(str,d2)))
    if ans1 < ans2:
        return 1
    else:
        return 0