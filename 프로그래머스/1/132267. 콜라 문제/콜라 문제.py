def solution(a, b, n):
    answer = 0

    while True:
        if n < a:
            break
        check = n%a
        n = n//a * b
        answer += n
        n = n + check

    return answer