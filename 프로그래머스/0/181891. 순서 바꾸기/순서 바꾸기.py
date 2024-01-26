def solution(lst, n):
    answer = lst[n:] + lst[:n]
    return answer