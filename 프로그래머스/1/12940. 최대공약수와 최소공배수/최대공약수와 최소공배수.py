def solution(n, m):
    answer = []
    a = max([n,m])
    b = min([n,m])
    while True:
        if a%b ==0:
            return [b, n*m / b]
        else:
            a, b=b, a % b
            
    return answer