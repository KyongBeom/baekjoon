N = int(input())
fruit_list = list(map(int, input().split()))

start = 0
answer = 0
count = [0] * 10
kinds = 0

for point in range(N):
    check = fruit_list[point]
    if count[check] == 0:
        kinds += 1
    count[check] += 1

    while kinds > 2:
        start_check = fruit_list[start]
        count[start_check] -= 1
        if count[start_check] == 0:
            kinds -= 1
        start += 1
    answer = max(answer, point - start + 1)

print(answer)
