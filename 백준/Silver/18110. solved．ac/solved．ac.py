n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

def round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
if n:
    lst.sort()
    check = round(n*0.15)
    print(round(sum(lst[check:n-check])/len(lst[check:n-check])))
else:
    print(0)