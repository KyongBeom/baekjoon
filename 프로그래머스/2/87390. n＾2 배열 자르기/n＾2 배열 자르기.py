def solution(n, left, right):
    answer =[]
    for i in range(left, right+1):
        check = i//n
        point = i%n
        answer.append(max(check,point)+1)
    return answer