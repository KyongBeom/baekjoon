

N, M = map(int, input().split())
lst = list(map(int, input().split()))
arr = [0]
sums = 0

for i in lst:
    sums += i
    arr.append(sums)

for i in range(M):
    A, B = map(int, input().split())
    print(arr[B] - arr[A-1])