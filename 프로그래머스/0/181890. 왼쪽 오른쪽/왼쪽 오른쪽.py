def solution(lst):

    for i in range(len(lst)):
        if lst[i] == "l":
            return lst[:i]
        elif lst[i] == "r":
            return lst[i+1:]
    
    return []
