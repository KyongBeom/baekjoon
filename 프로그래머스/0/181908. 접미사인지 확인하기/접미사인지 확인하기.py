def solution(my, is_suffix):
    answer = []
    for i in range(len(my)):
        answer.append(my[i:])
    answer.sort()
    for i in answer:
        if i == is_suffix:
            return 1
    return 0
