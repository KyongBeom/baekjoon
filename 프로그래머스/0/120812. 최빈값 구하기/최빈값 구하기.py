def solution(array):
    check = [0] * (max(array)+1)
    
    for i in array:
        check[i] += 1
    A = max(check)
    if check.count(A)>1:
        return -1
    else:
        return check.index(A)
    
