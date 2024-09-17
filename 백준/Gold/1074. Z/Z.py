import sys

n, r, c = map(int, sys.stdin.readline().split())

def answer(n, r, c):

	if n == 0:
		return 0
        
	return 2*(r%2)+(c%2) + 4*answer(n-1, r//2, c//2)

print(answer(n, r, c))