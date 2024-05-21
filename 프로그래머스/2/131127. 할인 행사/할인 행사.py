def solution(want, number, discount):
    answer = 0
    check = []
    for i in range(len(want)):
        for j in range(number[i]):
            check.append(want[i])
    check.sort()
    for i in range(len(discount) - 9):
        compare = discount[i : i + 10]
        compare.sort()
        if check == compare:
            answer += 1
    return answer