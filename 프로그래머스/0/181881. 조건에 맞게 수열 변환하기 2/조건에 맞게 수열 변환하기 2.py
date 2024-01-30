def solution(arr):
    cnt = 0
    i = 0
    while True:
        ans = []
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] %2 == 0:
                A = arr[i] /2
                ans.append(A)
            elif arr[i] < 50 and arr[i]%2 == 1:
                A = arr[i] *2 + 1
                ans.append(A)
            else:
                ans.append(arr[i])
        if ans == arr:
            return cnt
        cnt += 1
        arr = ans
    return cnt
        