T = int(input())

for tc in range(1,T+1):
    N = int(input())
    speed = 0
    res = 0
    for cnt in range(N):
        A = input().split()
        if A[0] == '0':
            pass
        elif A[0] == '1':
            speed += int(A[1])
        elif A[0] == '2':
            speed -= int(A[1])
        if speed < 0:
            speed = 0
        res += speed
    print(f'#{tc} {res}')