def solution(my, pat):
    cnt = 0
    for i in range(len(my)-len(pat)+1):
        if my[i:i+len(pat)] == pat:
           cnt += 1 
    return cnt