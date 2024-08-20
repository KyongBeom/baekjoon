def solution(k, tangerine):
    cnt = 0
    dic = {}
    for i in tangerine:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    for i in dic:
        if k <= 0:
            break
        else:
            k -= dic[i]
            cnt += 1
    return cnt