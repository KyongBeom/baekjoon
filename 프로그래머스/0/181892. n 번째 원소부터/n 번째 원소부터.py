def solution(lst, n):
    answer = []
    for i in range(n-1, len(lst)):
        answer.append(lst[i])
    return answer