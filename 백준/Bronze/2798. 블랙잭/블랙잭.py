import sys

N, M = map(int,sys.stdin.readline().split())
lst = list(map(int, input().split()))
solve = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            cnt = lst[i] + lst[j] + lst[k]
            if cnt > M:
                continue
            else:
                solve = max(solve,cnt)
print(solve)