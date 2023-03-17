def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1

N = int(input())

cnt = 0

arr = list(map(int, input().split()))

for i in arr:
    if i != 1:
        cnt += is_prime_number(i)
print(cnt)

