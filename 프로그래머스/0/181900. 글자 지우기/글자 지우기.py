def solution(my_string, indices):
    answer = list(my_string)
    for i in indices:
        answer[i] = ""
    answer = "".join(answer)
    return answer