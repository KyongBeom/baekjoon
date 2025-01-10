from collections import deque
import sys
n, m = map(int, sys.stdin.readline().strip().split())

ladder = {}
snake = {}

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    snake[u] = v

q = deque([1])
flag = [False] * 101
flag[1] = 0


while q:
    x = q.popleft()

    if x == 100:
        print(flag[x])
        break

    for i in range(1, 7):
        dx = x + i

        if dx <= 100 and flag[dx] ==  False:
            if dx in ladder.keys():
                dx = ladder[dx]
            if dx in snake.keys():
                dx = snake[dx]
            if flag[dx] == False:
                flag[dx] = flag[x] + 1 
                q.append(dx)