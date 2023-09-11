def solution(num_list):
    answer =0
    x = 1
    y = 0
    
    for i in num_list:
        x *= i
        y += i
    y= y**2
    print(y)
    if x < y:
        answer = 1
    
    return answer