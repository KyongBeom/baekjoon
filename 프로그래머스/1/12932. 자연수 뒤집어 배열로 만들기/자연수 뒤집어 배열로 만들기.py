def solution(n):
    answer = []
    x = str(n)[::-1]
    for i in x:
        answer.append(int(i))
    return answer