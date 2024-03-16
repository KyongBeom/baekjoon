def solution(s):
    answer = s.split(" ")
    ans = ""
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if j%2:
                ans += answer[i][j].lower()
            else:
                ans += answer[i][j].upper()
        if i == len(answer)-1:
            break
        else:
            ans += " "
    return ans