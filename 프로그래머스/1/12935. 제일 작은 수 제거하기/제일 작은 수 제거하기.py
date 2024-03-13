def solution(arr):
    if len(arr) <= 1:
        return [-1]
    answer = sorted(arr)
    arr.pop(arr.index(answer[0]))
    return arr