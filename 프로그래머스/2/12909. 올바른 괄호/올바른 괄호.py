

def solution(s):
    answer = True
    lst = list()
    for i in range(len(s)):
        if s[i] == "(":
            lst.append("(")
        else:
            if lst:
                lst.pop()
            else:
                return False
    return lst == []