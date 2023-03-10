
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    ans = []
    res = 0
    cnt = 0
    cnt2 = 0
    start = 0
    if N > M:
        while True:
            res += ai[cnt]*bj[cnt2]
            cnt += 1
            cnt2 += 1
            if cnt2 == M:
                if cnt == N:
                    ans.append(res)
                    break
                start += 1
                cnt2 = 0
                cnt = start
                ans.append(res)
                res = 0
    else:
        while True:
            res += ai[cnt]*bj[cnt2]
            cnt += 1
            cnt2 += 1
            if cnt == N:
                if cnt2 == M:
                    ans.append(res)
                    break
                start += 1
                cnt = 0
                cnt2 = start
                ans.append(res)
                res = 0
    print(f'#{tc} {max(ans)}')