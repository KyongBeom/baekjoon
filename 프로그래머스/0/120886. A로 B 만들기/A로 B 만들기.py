def solution(before, after):
    answer = 1
    before = sorted(before)
    after = sorted(after)
    for i in range(len(before)):
        if before[i] != after[i]:
            return 0
    return answer