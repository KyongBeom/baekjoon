def solution(x, n):
    answer = []
    z = x
    i = 0
    while i < n:
        answer.append(x)
        x += z
        i += 1
    return answer