def solution(a, b, c):
    if a == b == c:
        answer = (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)

    elif a == b != c or a==c !=b or a!=b==c:
        answer = (a+b+c)*(a**2+b**2+c**2)
    else:
        answer = a+b+c
    return answer