def solution(s):
    answer = ''
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    for i in dict:
        if dict[i] == 1:
            answer += i
    answer = sorted(answer)
    return "".join(answer)