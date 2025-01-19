n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = [0]*m

def back(k, x):
    if k == m:
        print(*answer)
        return

    check = 0
    for i in range(x, n):
        if check != arr[i]:
            answer[k] = arr[i]
            check = arr[i]
            back(k+1, i)

back(0, 0)