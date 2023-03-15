def binary_search(target):
    global N
    start = 1
    end = max(target)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for  i in target:
            cnt += i//mid
        if cnt >= N:
            start = mid + 1
        else:
            end = mid -1

    return end
K, N = map(int,input().split())  # K <= N
# K개에 걸쳐 랜선의 길이
len_list = []

for i in range(K):
    len_list.append(int(input()))


print(binary_search(len_list))
