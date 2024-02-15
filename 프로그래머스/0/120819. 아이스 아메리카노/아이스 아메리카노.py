def solution(money):
    answer = []
    a = 0
    b = 0
    while True:
        if money >= 5500:
            money -= 5500
            a += 1
        else:
            b = money
            break
    return [a,b]