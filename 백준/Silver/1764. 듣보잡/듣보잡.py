import sys

N, M = map(int, sys.stdin.readline().split())
arr = set()
arr2 = set()
for i in range(N):
    arr.add(input())
for j in range(M):
    arr2.add(input())
ans = sorted(list(arr&arr2))
print(len(ans))
for i in range(len(ans)):
    print(ans[i])