def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] > 1:
            check = food[i] // 2
            answer += str(i) * check
    answer = answer + "0" + answer[::-1]
    return answer