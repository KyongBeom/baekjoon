def solution(s):
    answer = []
    for i in s:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
    return answer