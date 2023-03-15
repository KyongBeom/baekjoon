x, y, w, h = map(int,input().split())
res = []

res.append(x)
res.append(y)
res.append(w-x)
res.append(h-y)
print(min(res))