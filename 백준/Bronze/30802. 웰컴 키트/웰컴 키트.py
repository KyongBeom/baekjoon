N = int(input())
lst_T = list(map(int, input().split()))
T, P = map(int, input().split())
cnt = 0
for i in lst_T:
    if i%T == 0:
        cnt += i//T
    else:
        cnt += i//T+1 

print(cnt)
ans = [N//P, N%P]
print(*ans)