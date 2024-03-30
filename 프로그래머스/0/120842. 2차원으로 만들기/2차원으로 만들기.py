def solution(num_list, n):
    answer = []
    k = 0
    i = n
    check = 0
    x = len(num_list)//n
    while check <x:
        answer.append(num_list[k:i])
        k += n
        i += n
        check += 1
    return answer