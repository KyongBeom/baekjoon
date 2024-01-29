def solution(num_list):
    num_1 = 0
    num_2 = 0
    
    for i in range(len(num_list)):
        if i %2:
            num_1 += num_list[i]
        else:
            num_2 += num_list[i]
    
    if num_1 >= num_2:
        return num_1
    else:
        return num_2