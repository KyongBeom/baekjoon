def solution(s):
    answer = ''
    check = s.split()
    change = []
    for i in check:
        change.append(int(i))
    answer += str(min(change))
    answer += " "
    answer += str(max(change))
    return answer