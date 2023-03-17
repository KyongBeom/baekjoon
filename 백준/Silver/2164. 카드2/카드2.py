import sys
from collections import deque
N = int(sys.stdin.readline())

arr = deque([i for i in range(N,0,-1)])
while len(arr) > 1:
    arr.pop()
    arr.appendleft(arr.pop())
print(arr[0])