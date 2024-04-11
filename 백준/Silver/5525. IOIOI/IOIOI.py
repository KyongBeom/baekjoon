n = int(input())
m = int(input())
arr = input()
p = "IOI"
cnt = 0
if n >= 2:
    for i in range(n-1):
        p += "OI"

for i in range(m - 3 + 2 * n):
    if arr[i:i+len(p)] == p:
        cnt += 1
print(cnt)