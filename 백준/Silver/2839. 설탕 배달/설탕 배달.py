import sys
N = int(sys.stdin.readline())
cnt = 0

while N >=0:
    if N %5 == 0:  # 0으로 떨어질 때도 작동함
        cnt += (N//5)
        print(cnt)
        break
    N -= 3
    cnt += 1
else:  # while 이 정상적으로 끝나면 N이 음수
    print(-1)


