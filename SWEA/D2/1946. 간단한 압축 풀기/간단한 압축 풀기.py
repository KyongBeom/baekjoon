T = int(input())
for tc in range(1,T+1):
    N = int(input())
    res = [0]
    for i in range(N):
        A, B = input().split()
        B = int(B)
        for j in range(B):
            res.append(A)
    print(f'#{tc}')
    for i in range(1,len(res)):
        print(res[i],end='')
        if i%10 == 0:
           print()
    print()