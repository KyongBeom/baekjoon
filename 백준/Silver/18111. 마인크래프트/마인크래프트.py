import sys
N, M, B = map(int, sys.stdin.readline().split())

arr= [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = 100000000000000
for i in range(257):
    play_1, play_2 = 0, 0

    for j in range(N):
        for k in range(M):
            if arr[j][k] > i:
                play_1 += arr[j][k] - i
            else:
                play_2 += i - arr[j][k]
    if play_2 > play_1+B:
        continue

    cnt = play_1 * 2 + play_2

    if cnt <= ans:
        ans = cnt
        top = i

print(ans, top)