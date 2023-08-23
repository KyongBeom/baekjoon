# 변환을 하면 cnt +1
# 1,2 가 나오면 stop

A = input()
cnt = 0

while len(A) > 1:
    B = 0
    cnt += 1
    for i in A:
        B += int(i)
    A = str(B)

print(cnt)
if int(A) %3 == 0:
    print('YES')
else:
    print("NO")

    