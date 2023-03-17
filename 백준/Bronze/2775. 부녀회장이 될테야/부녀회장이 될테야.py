t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    res = [i for i in range(1,n+1)]
    for i in range(k):
        for j in range(1, n):
            res[j] += res[j-1]
    print(res[-1])

