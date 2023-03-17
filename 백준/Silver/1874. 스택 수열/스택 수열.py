import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for i in range(N)]
idx = 0
i = 0
stack = []
answer = []
while idx < N:
    if lst[idx] > i:
        i += 1
        stack.append(i)

        answer.append('+')
    elif lst[idx] <= i:
        if lst[idx] != stack.pop():
            answer = ['NO']
            break
        answer.append('-')
        idx += 1

for i in answer:
    print(i)