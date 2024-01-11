def solution(arr, queries):
    answer = []

    for idx in queries:
        check = 10000000000
        for i in range(len(arr)):
            if idx[0] <= i <= idx[1] and idx[2] < arr[i]:
                if check > arr[i]:
                    check = arr[i]
        if check == 10000000000:
            check = -1
        answer.append(check)
    return answer