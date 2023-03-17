import math
A, B, V = map(int,input().split())


res =math.ceil((V-A)/(A-B))
print(res+1)