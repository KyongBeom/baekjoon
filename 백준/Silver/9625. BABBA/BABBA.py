K = int(input())

dpA = [0]  * 47
dpB = [0]  * 47

dpA[2] = 1

for i in range(3, K+2):
    dpA[i] = dpA[i-1] + dpA[i-2]


print(dpA[K], dpA[K+1])