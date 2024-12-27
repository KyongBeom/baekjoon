N = int(input())
arr = list(map(int, input().split()))
check = sorted(set(arr))

dic = {}
for i in range(len(check)):
    dic[check[i]] = i

answer = []
for i in range(N):
    answer.append(dic[arr[i]])
print(*answer)