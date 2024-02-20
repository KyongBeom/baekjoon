a = input()
answer = ""
for i in a:
    if i.islower():
        answer += i.upper()
    else:
        answer += i.lower()
print(answer)