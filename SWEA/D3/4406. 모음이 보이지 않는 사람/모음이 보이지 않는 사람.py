T = int(input())
for tc in range(1,T+1):
    N = input()
    res =''
    for i in N:
        if i not in 'aeiou':
            res += i
    print(f'#{tc} {res}')