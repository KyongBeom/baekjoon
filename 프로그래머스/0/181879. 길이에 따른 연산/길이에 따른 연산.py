def solution(lst):
    answer = 0
    if len(lst) >= 11:
        return sum(lst)
    else:
        ans = 1
        for i in lst:
            ans *=i
        return ans