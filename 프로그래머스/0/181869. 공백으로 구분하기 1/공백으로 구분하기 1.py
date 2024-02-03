def solution(my):
    answer = []
    check = 0
    for i in range(len(my)):
        if my[i] == " ":
            answer.append(my[check:i])
            check = i+1
    answer.append(my[check:])
    return answer