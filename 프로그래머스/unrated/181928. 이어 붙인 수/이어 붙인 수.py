def solution(num_list):
    answer = 0
    holsu = ""
    jacksu = ""
    for i in num_list:
        if i %2:
            holsu += str(i)
        else:
            jacksu += str(i)
    answer = int(holsu) + int(jacksu)
    return answer