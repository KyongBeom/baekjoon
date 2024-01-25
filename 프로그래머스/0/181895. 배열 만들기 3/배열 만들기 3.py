def solution(arr, intervals):
    answer = []
    for i in intervals:
        for k in range(i[0],i[1]+1):
            answer.append(arr[k])
    return answer