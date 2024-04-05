def solution(emergency):
    dict = {}
    answer = []
    check = sorted(emergency, reverse = True)

    for i in range(len(emergency)):
        dict[check[i]] = i+1
    for i in range(len(dict)):
        answer.append(dict[emergency[i]])
    return answer