N = int(input())
first = list(input())
for i in range(N-1):
    other = list(input())
    for j in range(len(first)):
        if first[j] != other[j]:
            first[j] = "?"
print(''.join(first))