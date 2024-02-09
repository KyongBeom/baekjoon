def solution(n_str):
    answer = ''
    check = True
    for i in n_str:
        if check and i =="0":
            pass
        else:
            check = False
            answer += i
    return answer