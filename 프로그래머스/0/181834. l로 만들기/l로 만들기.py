def solution(my):
    answer = ''
    for i in my:
        if ord(i) < ord("l"):
            answer += "l"
        else:
            answer += i
    return answer