n = int(input())
arr = [input().split() for i in range(n)]

answer = []

def dp(i,j ,n):
    check = arr[i][j]
    for a in range(i, i+n):
        for b in range(j, j+n):
            if check != arr[a][b]:
                dp(i, j, n// 2)
                dp(i+n//2, j+n//2, n // 2)
                dp(i+n//2, j, n // 2)
                dp(i, j+n//2, n // 2)
                return
    if check == "0":
        answer.append(0)
    else:
        answer.append(1)

dp(0,0,n)

print(answer.count(0))
print(answer.count(1))
