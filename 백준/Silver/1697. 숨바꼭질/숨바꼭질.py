from collections import deque

A, B = map(int, input().split())
check = [0] * 1000001

queue = deque()
queue.append(A)
answer = 0
while queue:
    x = queue.popleft()
    if x == B:
        answer = check[x]
        break
    for i in (x-1, x+1, 2*x):
        if 0<= i <= 1000000 and not check[i]:
            check[i] = check[x] + 1
            queue.append(i)

print(answer)