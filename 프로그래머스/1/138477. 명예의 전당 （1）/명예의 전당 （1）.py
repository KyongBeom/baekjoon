
def solution(k, score):
    answer = []
    check = []
    
    for i in range(len(score)):
        check.append(score[i])
        check = sorted(check, reverse = True)
        if len(check) > k:
            check.pop()
        answer.append(check[-1])
    return answer