res = []
for tc in range(10):
    N = int(input())
    res.append(N%42)
res = list(set(res))
print(len(res))