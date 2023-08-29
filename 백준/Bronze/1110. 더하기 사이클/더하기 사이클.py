N = int(input())
check = N

cnt = 0

A = 987654321

while N != A:
    x = check // 10
    y = check % 10
    z = (x+y) % 10
    check = (y*10) + z
    A = check
    cnt += 1

print(cnt)