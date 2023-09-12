def solution(a, d, included):
    answer = 0
    cnt = a
    lst = []
    for i in range(len(included)): 
        if i == 0:
            lst.append(cnt)
        else:
            cnt += d
            lst.append(cnt)

    for i in range(len(included)):
        if included[i] == True:
            answer += lst[i]
            
    return answer