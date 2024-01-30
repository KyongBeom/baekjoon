def solution(lst):
    cnt = 0
    for i in lst:
        while i != 1:
            if i %2 == 0:
                i = i / 2
                cnt += 1
            else:
                i = (i-1)/2
                cnt += 1
    return cnt