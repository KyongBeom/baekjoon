import sys

T = int(sys.stdin.readline())
S = set()
for tc in range(T):
    N = sys.stdin.readline().split()
    if len(N) == 1:
        if N[0] == 'all':
            S = set(i for i in range(1, 21))
        else:
            S = set()
    else:
        x, y = N[0], N[1]
        y = int(y)
        if x == 'add':
            S.add(y)
        elif x == 'remove':
            S.discard(y)
        elif x == 'check':
            if y in S:
                print(1)
            else:
                print(0)
        elif x == 'toggle':
            if y in S:
                S.discard(y)
            else:
                S.add(y)
