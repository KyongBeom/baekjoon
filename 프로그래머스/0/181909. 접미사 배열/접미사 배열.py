def solution(my):
    answer= []
    for i in range(len(my)):
        answer.append(my[i:])
    answer.sort()
    return answer