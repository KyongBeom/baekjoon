N = int(input())
M = int(input())
S = input()

word = "IOI"
start = 0
ans = 0
check = 0


while start < (M-1):
    if S[start:start+3] == word:
        start += 2
        check += 1
        if check == N:
            ans += 1
            check -= 1
    else:
        start += 1
        check = 0
print(ans)