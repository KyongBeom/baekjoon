def solution(cards1, cards2, goal):

    check = []
    
    i = 0
    j = 0
    k = 0
    while k < len(goal):
        if  i < len(cards1) and goal[k] == cards1[i]:
            check.append(cards1[i])
            i += 1
        if  j < len(cards2) and goal[k] == cards2[j]:
            check.append(cards2[j])
            j += 1
        
        k += 1

    
    if check == goal:
        return "Yes"
    else:
        return "No"
