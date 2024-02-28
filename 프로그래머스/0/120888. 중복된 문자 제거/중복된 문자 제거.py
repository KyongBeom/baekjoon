def solution(my):
    answer = ''
    for i in my:
        if i not in answer:
            answer+=i
    return answer