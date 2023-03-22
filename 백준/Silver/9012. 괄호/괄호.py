N = int(input())

for i in range(N):
    stack = []
    A = input()
    ans = 'YES'
    for j in A:
        if j == '(':
            stack.append('(')
        elif stack and stack[-1] =='(' and j == ')':
            stack.pop()
        elif not stack and j == ')':
            stack.append(j)
            break
    if stack:
        print('NO')
    else:
        print("YES")