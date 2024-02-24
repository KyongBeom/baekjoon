def solution(n):
    answer = []
    for i in range(n):
        check = []
        for j in range(n):
            if i == j:
                check.append(1)
            else:
                check.append(0)
        answer.append(check)
    return answer