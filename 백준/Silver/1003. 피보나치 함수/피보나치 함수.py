import sys

N = int(sys.stdin.readline())
for i in range(N):
    A = int(sys.stdin.readline())
    fibo_zero = 1
    fibo_one = 0
    for j in range(A):
        fibo_zero, fibo_one = fibo_one, fibo_zero+fibo_one
    print(fibo_zero,fibo_one)
