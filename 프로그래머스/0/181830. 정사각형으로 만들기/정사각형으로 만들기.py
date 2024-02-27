def solution(arr):
    i = len(arr)
    j = len(arr[0])
    if i > j:
        for k in range(len(arr)):
            for x in range(i-j):
                arr[k].append(0)
    elif j > i:
        for z in range(j-i):
            arr.append([0]*j)

    return arr