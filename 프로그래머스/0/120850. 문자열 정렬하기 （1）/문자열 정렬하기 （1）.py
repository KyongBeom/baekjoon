def solution(my):
    answer = []
    for i in my:
        if i in "0123456789":
            answer.append(int(i))
    answer = sorted(answer)
    return answer