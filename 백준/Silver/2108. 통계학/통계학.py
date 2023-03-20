N = int(input())
lst = []
arr = [0] * 8001
for tc in range(N):
    A = int(input())
    arr[A] += 1
    lst.append(A)
lst.sort()
middle_point = lst[N//2]
cnt = 0
middle = round(sum(lst) / N)
rang = max(lst) - min(lst)
print(middle)
print(middle_point)

dic = dict()
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

maxs = max(dic.values())
maxs_dic = []

for i in dic:
    if maxs == dic[i]:
        maxs_dic.append(i)

if len(maxs_dic) > 1:
    print(maxs_dic[1])
else:  # 하나라면
    print(maxs_dic[0])


print(rang)