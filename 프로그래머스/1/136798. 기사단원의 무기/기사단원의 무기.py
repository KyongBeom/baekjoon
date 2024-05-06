def solution(number, limit, power):
    answer = 0
    check = []
    
    
    for n in range(1, number+1):
        cnt = 0
        for i in range(1, int(n**(1/2)) + 1):
            if (n % i == 0):
                cnt += 1
                if ( (i**2) != n) : 
                    cnt += 1

        check.append(cnt)
    
    for i in range(len(check)):
        if check[i] > limit:
            check[i] = power
        
    return sum(check)