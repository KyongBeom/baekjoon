import heapq
import sys
stdin = sys.stdin
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    check = int(sys.stdin.readline())
    if check != 0:
        heapq.heappush(heap, check)
    else:
        if heap:
            result = heapq.heappop(heap)
            print(result)
        else:
            print(0)
