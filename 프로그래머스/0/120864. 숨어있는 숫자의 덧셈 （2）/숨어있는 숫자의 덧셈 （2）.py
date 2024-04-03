def solution(my_string):
    answer = ""
    for i in my_string:
        if i.isdigit():
            answer += i
        else:
            answer += " "
    check = sum(list(map(int,answer.split())))
    
    return check