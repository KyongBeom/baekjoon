T = int(input())
stack = []

for i in range(T):
    N = int(input())

    if stack and N == 0:
        stack.pop()
    else:
        stack.append(N)
print(sum(stack))