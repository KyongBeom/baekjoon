import sys

N = int(sys.stdin.readline())

for i in range(N):
    A = int(sys.stdin.readline())
    lst = [0] * (A+1)   
    for i in range(1,A+1):
        if i < 4:
            lst[i] = 1
        else:
            lst[i] = lst[i-2] + lst[i-3]
    print(lst[-1])
