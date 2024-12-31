n = int(input())

arr = []

for i in range(n):
    check = list(map(int, input().split()))
    arr.append(check)

arr = sorted(arr, key=lambda x:(x[1], x[0]))
point = 0
answer = 0

for start, end in arr:
    if point <= start:
        answer += 1
        point = end
print(answer)