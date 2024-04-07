N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

for j in range(1, N):
    arr[j][0] = min(arr[j-1][1], arr[j-1][2]) + arr[j][0]
    arr[j][1] = min(arr[j-1][0], arr[j-1][2]) + arr[j][1]
    arr[j][2] = min(arr[j-1][0], arr[j-1][1]) + arr[j][2]

print(min(arr[N-1]))