from collections import deque
import sys

point = deque()
n = int(input())
ans1 = -1

for i in range(n):
    queue = sys.stdin.readline().split()

    if queue[0] == "push_front":
        point.appendleft(queue[1])
    elif queue[0] == "push_back":
        point.append(queue[1])
    elif queue[0] == "pop_front":
        if point:
            print(point[0])
            point.popleft()
        else:
            print(ans1)
    elif queue[0] == "pop_back":
        if point:
            print(point.pop())
        else:
            print(ans1)
    elif queue[0] == "size":
        print(len(point))
    elif queue[0] == "empty":
        if point:
            print("0")
        else:
            print("1")
    elif queue[0] == "front":
        if point:
            print(point[0])
        else:
            print(ans1)
    elif queue[0] == "back":
        if point:
            print(point[-1])
        else:
            print(ans1)