T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))

    D = round(sum(arr) / len(arr))
    print(f'#{tc} {D}')