def solution(arr, queries):
    for idx in queries:
        for i in range(idx[0], idx[1] +1) :
            if i % idx[2] == 0:
                arr[i] += 1
    return arr
