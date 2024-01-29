def solution(todo, check):
    answer = []
    for i in range(len(todo)):
        if check[i]==False:
            answer.append(todo[i])
    return answer