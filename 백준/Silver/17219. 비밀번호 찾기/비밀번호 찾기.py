import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
dict = {}
for i in range(N):
    A, B = input().split()
    dict[A] = B

for j in range(M):
    A = input().rstrip()
    print(dict[A])
