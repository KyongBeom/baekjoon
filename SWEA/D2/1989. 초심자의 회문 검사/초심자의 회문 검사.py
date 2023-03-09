T = int(input())
for tc in range(1,T+1):
    a = input()
    b = a[::-1]
    if a == b:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')