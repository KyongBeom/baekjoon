n = int(input())

cnt = 0
base = 666
while True:
    if '666' in str(base):
        cnt += 1
    if cnt == n:
        print(base)
        break
    base += 1