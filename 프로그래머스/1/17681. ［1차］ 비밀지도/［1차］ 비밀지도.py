def solution(n, arr1, arr2):
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        if len(arr1[i]) < n:
            arr1[i] = (n-len(arr1[i])) * "0" + arr1[i]
        arr2[i] = bin(arr2[i])[2:]
        if len(arr2[i]) < n:
            arr2[i] = (n-len(arr2[i])) * "0" + arr2[i]
    answer = []
    for i in range(n):
        check = ""
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                check += '#'
            else:
                check += ' '
        answer.append(check)
    return answer