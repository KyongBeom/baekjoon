def solution(n, slicer, lst):
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]
    answer = []
    if n == 1:
        for i in range(b+1):
            answer.append(lst[i])
    elif n == 2:
        for i in range(a, len(lst)):
            answer.append(lst[i])
    elif n == 3:
        for i in range(a, b+1):
            answer.append(lst[i])
    else:
        for i in range(a,b+1, c):
            answer.append(lst[i])
    return answer