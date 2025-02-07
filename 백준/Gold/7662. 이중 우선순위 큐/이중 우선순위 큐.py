import sys
import heapq

input = sys.stdin.readline

def heapchecks(heap, removed):
    while heap and removed[heap[0][1]]:
        heapq.heappop(heap)

tc = int(input())
for _ in range(tc):
    k = int(input())
    min_heap = []
    max_heap = []
    removed = {}

    for i in range(k):
        cmd, num = input().split()
        num = int(num)

        if cmd == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            removed[i] = False

        elif cmd == "D":
            if num == 1:
                heapchecks(max_heap, removed)
                if max_heap:
                    removed[max_heap[0][1]] = True
                    heapq.heappop(max_heap)
            else: 
                heapchecks(min_heap, removed)
                if min_heap:
                    removed[min_heap[0][1]] = True
                    heapq.heappop(min_heap)

    heapchecks(min_heap, removed)
    heapchecks(max_heap, removed)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")