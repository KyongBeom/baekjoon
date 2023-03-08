T = int(input())
for tc in range(1,T+1):
    N = int(input())
    K = list(map(int,input().split()))
    K.sort()
    print(f'#{tc}', *K)