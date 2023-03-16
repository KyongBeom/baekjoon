N = int(input())
start = 1
cnt = 1
while N > start:
    start += cnt * 6
    cnt += 1
print(cnt)
    

