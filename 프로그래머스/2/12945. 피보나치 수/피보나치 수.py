def solution(n):
    check = [0,1]
    for i in range(2,n+1):
        check.append((check[i-1]+check[i-2])%1234567)
    return check[-1]