import heapq
import sys
N = int(sys.stdin.readline())

lst = []

heapq.heapify(lst)
for i in range(N):
    A = int(sys.stdin.readline())

    if A == 0:
        if lst:
            ans = heapq.heappop(lst)[1]
            print(ans)
        else:
            print(0)
    else:
        heapq.heappush(lst,(-A,A))
