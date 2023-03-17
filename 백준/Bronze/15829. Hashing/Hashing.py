import sys

N = int(input())
res = 0
arr = list(input())
for i in range(N):
    res += (ord(arr[i])-96)*31**i
print(res)