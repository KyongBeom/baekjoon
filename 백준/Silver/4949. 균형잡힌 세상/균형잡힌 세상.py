while True:
    A = input()
    stack = []
    ans = ''
    if A == '.':
        break
    for i in A:
        if i == '(' or i =='[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print('no')
    else:
        print('yes')