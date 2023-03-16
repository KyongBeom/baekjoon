import sys
N = int(sys.stdin.readline())
s = []

for i in range(N):
    A = sys.stdin.readline().split()
    if A[0] == 'push':
        s.append(A[1])
    elif A[0] == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif A[0] == 'size':
        print(len(s))
    elif A[0] == 'empty':
        if s:
            print(0)
        else:
            print(1)
    elif A[0] == 'top':
        if s:
            print(s[-1])
        else:
            print(-1)