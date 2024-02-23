def solution(my):
    answer =0
    for i in my:
        if i in "123456789":
            answer += int(i)
    return answer