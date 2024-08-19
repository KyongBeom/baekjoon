def lcd(a,b):
    x, y = a, b
    while b>0:
        a, b = b, a%b
    check = a
    return x * y / check


def solution(arr):
    answer = arr[0]
    for i in range(len(arr)-1):
        answer = lcd(answer, arr[i+1])
    return answer