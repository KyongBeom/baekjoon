def solution(n):
    n = str(n)
    check = list(n)
    
    return int("".join(sorted(check, key=lambda x:x,reverse=True)))