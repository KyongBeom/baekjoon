from collections import deque
import sys

tc = int(input())
for i in range(tc):
    AC = sys.stdin.readline().strip()
    length = int(sys.stdin.readline())
    lst = deque(sys.stdin.readline().strip()[1:-1].split(","))
    if length == 0:
       lst = deque()
    answer = 0
    check = 0
    for i in AC:
        if i == "R":
            check += 1
        elif i == "D":
            if lst:
                if check %2 == 0 :
                    lst.popleft()
                else:
                    lst.pop()
            else:
                answer = "error"
                break

    if answer == "error":
        print(answer)
    else:
        if check % 2:
            lst.reverse()
            print("[" + ",".join(lst) + "]")
        else:
            print("[" + ",".join(lst) + "]")
