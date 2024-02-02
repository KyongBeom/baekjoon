def solution(arr):
    answer = []
    for i in range(len(arr)):
        if "ad" not in arr[i]:
            answer.append(arr[i])
    return answer