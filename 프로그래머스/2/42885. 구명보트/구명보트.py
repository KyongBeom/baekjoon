def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    for j in range(len(people)-1,-1, -1):
        if i < j and people[i]+people[j] <=limit:
            answer += 1
            i += 1
    
    return len(people) - answer