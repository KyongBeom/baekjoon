N = int(input())
res = []
for i in range(N):
    res.append(input())
res = list(set(res))
res.sort()
res.sort(key = lambda x:len(x))
for i in res:
    print(i)