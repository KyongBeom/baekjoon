N = int(input())  # 약수의 개수
lst = list(map(int, input().split()))
lst.sort()

a =lst[0]
b = lst[-1]
print(a*b)