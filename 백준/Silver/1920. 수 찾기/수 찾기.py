N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()
ans = []
for i in arr2:
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if i == arr1[mid]:
            ans.append(1)
            break
        elif i > arr1[mid]:
            start = mid + 1
        else:
            end = mid - 1
    else:
        ans.append(0)
for i in ans:
    print(i)
    