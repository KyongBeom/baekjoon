import heapq
import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    A = int(sys.stdin.readline())

    if A == 0 and lst:
        print(heapq.heappop(lst)[1])
        
    elif A != 0:
        heapq.heappush(lst, (abs(A),A))
    else:
        print(0)
    
