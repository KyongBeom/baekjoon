def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        check = []
        for j in range(len(arr2[0])):
            point = 0
            for k in range(len(arr1[0])):
                point += arr1[i][k] * arr2[k][j]
            check.append(point)
        answer.append(check)    
    return answer
