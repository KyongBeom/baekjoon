def solution(my, pat):
    answer = ""
    for i in pat:
        if i == "A":
            answer += "B"
        else:
            answer += "A"
    if answer in my:
        return 1
    else :
        return 0
