lst = input().split("-")

check = 0
for i in lst[0].split('+'):
    check += int(i)
for i in lst[1:]:
    for j in i.split("+"):
        check -= int(j)

print(check)

