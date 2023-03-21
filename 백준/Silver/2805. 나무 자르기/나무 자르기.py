import sys
N,M = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start = 1
end = max(arr)
while start <= end:
    cnt = 0
    middle = (start + end) // 2
    for i in arr:
        if i >= middle:
            cnt += i - middle

    if cnt >= M:
        start = middle + 1
    else:
        end = middle -1
print(end)
