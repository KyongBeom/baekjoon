def solution(n):
    answer = 1
    x = 6
    while True:
        if x % n == 0:
            return answer
        else:
            answer += 1
            x = x + 6
    return answer