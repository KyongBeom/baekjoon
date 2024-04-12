n = int(input())
for i in range(n):
    m = int(input())
    dict = {}
    for i in range(m):
        name, type = input().split()
        if type in dict:
            dict[type] += 1
        else:
            dict[type] = 1
    cnt = 1

    for i in dict:
        cnt *= (dict[i] + 1)
    print(cnt -1)
