def solution(x):
    t = str(x)
    answer = 0
    for i in t:
        answer += int(i)
    if x%answer:
        return False
    return True