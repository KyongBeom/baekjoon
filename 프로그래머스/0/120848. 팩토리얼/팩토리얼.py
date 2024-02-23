def solution(n):
    answer = 1
    fac = 1
    while fac <= n:
        answer += 1
        fac *= answer
    return answer -1