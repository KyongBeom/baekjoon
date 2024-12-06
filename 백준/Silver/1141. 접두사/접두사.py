n = int(input())
arr = [input() for _ in range(n)]
arr = sorted(arr, key = len)
answer = n
for i in range(n):
    check = arr[i]
    for j in range(i+1, n):
        check2 = arr[j][:len(check)]
        if check == check2:
            answer -= 1
            break
print(answer)

