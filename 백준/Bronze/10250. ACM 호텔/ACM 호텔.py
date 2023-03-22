T = int(input())

for tc in range(1,T+1):
    H, W, N = map(int, input().split())
    A = N % H
    B = N//H+1
    if A == 0:
        A=H
        B = N//H
    print(A*100+B)