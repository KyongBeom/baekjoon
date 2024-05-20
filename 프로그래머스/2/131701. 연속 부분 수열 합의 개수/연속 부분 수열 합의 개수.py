def solution(elements):
    answer = []
    
    check_point = elements * 2
    
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.append(sum(check_point[j:j+i+1]))
    
    return len(set(answer))