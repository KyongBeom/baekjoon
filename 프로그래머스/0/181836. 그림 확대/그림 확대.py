def solution(picture, k):
    answer = []
    
    for i in picture: 
        check = ''
        
        for j in i:
            check += j * k
        
        for _ in range(k):
            answer.append(check)
    
    return answer