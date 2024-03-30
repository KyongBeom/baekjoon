def solution(my, m, c):
    answer = ""
    for i in range(len(my)):
        if i%m == c-1:
            answer += my[i]
    return answer