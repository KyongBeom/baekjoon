def solution(name, yearning, photo):
    answer = []
    for i in photo:
        cnt = 0
        for j in i:
            for x in range(len(name)):
                if j == name[x]:
                    cnt += yearning[x]
        answer.append(cnt)
    return answer