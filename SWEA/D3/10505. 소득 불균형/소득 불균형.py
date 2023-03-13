T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    avr = sum(arr)/N
    cnt = 0
    for i in range(N):
        if arr[i] <= avr:
            cnt += 1
    print(f'#{tc} {cnt}')