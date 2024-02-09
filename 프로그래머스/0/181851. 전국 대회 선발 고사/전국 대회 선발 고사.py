def solution(rank, attendance):
    answer = []
    for i in range(len(rank)):
        if attendance[i]:
            answer.append([i, rank[i]])
    answer.sort(key = lambda x : x[1])
    return 10000 * answer[0][0] + 100 * answer[1][0] + answer[2][0]