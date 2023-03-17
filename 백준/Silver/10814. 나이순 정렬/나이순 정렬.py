import sys
N = int(sys.stdin.readline())
res = []
for tc in range(N):
    A, B = sys.stdin.readline().split()
    D = [int(A),B,tc]
    res.append(D)
res.sort(key=lambda x:[x[0],x[2]])
for tc in res:
    print(tc[0],tc[1])