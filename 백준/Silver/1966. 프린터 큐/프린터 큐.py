T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    M_q = [0] * N
    M_q[M] = 1
    cnt = 0
    while True:
        if queue[0] != max(queue):
            queue.append(queue.pop(0))
            M_q.append(M_q.pop(0))
        else:
            cnt += 1
            queue.pop(0)
            if M_q.pop(0) == 1:
                print(cnt)
                break
