N = int(input())
res = []
for i in range(1, N):
    M = 0
    i = str(i)
    for j in i:
        M += int(j)
    M += int(i)
    if M == N:
        res.append(i)
        break
if res:
    print(res[0])
else:
    print(0)

