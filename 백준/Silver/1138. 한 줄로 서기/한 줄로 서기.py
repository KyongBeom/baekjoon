N = int(input())
M = list(map(int, input().split()))

lst  = [0] * N
for i in range(N):
    cnt = 0

    for j in range(N):
        if cnt == M[i] and lst[j] == 0:
            lst[j] = i+1
            break
        
        elif lst[j] == 0:
            cnt += 1

print(*lst)