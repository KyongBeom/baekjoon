def solution(n, k):
    if n >= 10 and k:
        a = n // 10
        return n * 12000 + k * 2000 - 2000 * a
    else:
        return n * 12000 + k * 2000