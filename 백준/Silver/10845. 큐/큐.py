import sys
N = int(sys.stdin.readline())
q = []

for i in range(N):
    A = sys.stdin.readline().split()
    if A[0] == 'push':
        q.append(A[1])
    elif A[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif A[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif A[0] == 'size':
        print(len(q))
    elif A[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif A[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
