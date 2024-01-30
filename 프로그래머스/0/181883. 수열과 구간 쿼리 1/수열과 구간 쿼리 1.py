def solution(arr, qur):
    answer = []
    for i in qur:
        for j in range(i[0],i[1]+1):
            arr[j] += 1
    return arr