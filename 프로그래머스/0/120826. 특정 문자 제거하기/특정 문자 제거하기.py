def solution(my , letter):
    answer = ''
    for i in range(len(my)):
        if my[i] == letter:
            pass
        else:
            answer += my[i]
    return answer