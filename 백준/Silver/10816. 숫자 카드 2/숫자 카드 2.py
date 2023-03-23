import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

card_list = list(map(int,sys.stdin.readline().split()))
cnt_dic = {}

for i in arr:
    if i in cnt_dic:
        cnt_dic[i] += 1
    else:
        cnt_dic[i] = 1

for i in card_list:
    try:
        print(cnt_dic[i], end=' ')
    except:
        print('0', end =' ')