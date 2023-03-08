T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    res = 0
    for i in range(9):
        if sum(arr[i]) == 45:
            res += 1
    for j in range(9):
        cnt2 = 0
        for i in range(9):
            cnt2 += arr[i][j]
        if cnt2 == 45:
            res += 1
    for i in range(0,9,3):
        for j in range(0,9,3):
            cnt = 0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    cnt += arr[k][l]
            if cnt == 45:
                res += 1
    if res == 27:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')