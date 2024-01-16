def solution(x1, x2, x3, x4):
    answer = True
    z1 = True
    z2 = True
    if x1 != x2:
        z1 = True
    elif x1 == x2 == True:
        z1 = True
    else:
        z1 = False
    
    if x3 != x4:
        z2 = True
    elif x3 == x4 == True:
        z2 = True
    else:
        z2 = False
        
    if z1 == z2 == True:
        answer= True
    else:
        answer = False
    return answer