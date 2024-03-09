def solution(i, j, k):
    answer = 0
    for x in range(i,j+1):
        for z in str(x):
            if z == str(k):
                answer += 1
    return answer