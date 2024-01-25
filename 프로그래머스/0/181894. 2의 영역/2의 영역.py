def solution(arr):
    answer = []
    check = []
    for i in range(len(arr)):
        if arr[i] == 2:
            check.append(i)
    if len(check) == 0:
        return [-1]
    else:
        for i in range(min(check),max(check)+1):
            answer.append(arr[i])
    return answer