arr = list(map(int, input().split()))
res = ''

for i in arr:
    res += str(i)
if res == '12345678':
    print('ascending')
elif res == '87654321':
    print('descending')
else:
    print('mixed')