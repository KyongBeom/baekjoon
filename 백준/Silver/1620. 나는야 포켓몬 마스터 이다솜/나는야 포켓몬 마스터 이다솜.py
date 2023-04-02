import sys

n,m = map(int, sys.stdin.readline().split())

dict = {}

for i in range(1,n+1):
    A = sys.stdin.readline().rstrip()
    dict[i] = A
    dict[A] = i
for i in range(m):
    B = sys.stdin.readline().rstrip()
    if B.isdigit():
        print(dict[int(B)])
    else:
        print(dict[B])