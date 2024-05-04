def solution(answers):
    answer = []

    men1 = [1,2,3,4,5]
    men2 = [2,1,2,3,2,4,2,5]
    men3 = [3,3,1,1,2,2,4,4,5,5]
    check = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == men1[i%len(men1)]:
            check[0] += 1
        if answers[i] == men2[i%len(men2)]:
            check[1] += 1
        if answers[i] == men3[i%len(men3)]:
            check[2] += 1

    for i in range(3):
        if check[i] == max(check):
            answer.append(i+1)
        
    return answer