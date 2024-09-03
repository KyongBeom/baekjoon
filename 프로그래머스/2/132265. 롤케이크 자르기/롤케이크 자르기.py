def solution(topping):
    count = 0
    a = {} # 동생꺼
    b = {} # 철수꺼
    for i in topping:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    
    for j in topping:
        if len(a) == len(b):
            count += 1
        
        if j not in b:
            b[j] = 1
        a[j] -= 1
        if a[j] == 0:
            del a[j]
    return count