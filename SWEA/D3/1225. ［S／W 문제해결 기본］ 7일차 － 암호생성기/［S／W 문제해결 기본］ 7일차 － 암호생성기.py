T = 10
for tc in range(1,T+1):
    K = int(input())
    arr = list(map(int, input().split()))
    i = 1
    while True:
        if i == 6:
            i = 1
        sol = arr.pop(0)
        arr.append(sol-i)
        i += 1
        if arr[-1] <= 0:
            arr[-1] = 0
            break
    print(f'#{tc}', *arr)