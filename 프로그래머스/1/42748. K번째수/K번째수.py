def solution(array, commands):
    answer = []
    for i, j, k in commands:
        check = sorted(array[i-1:j])
        answer.append(check[k-1])
    return answer