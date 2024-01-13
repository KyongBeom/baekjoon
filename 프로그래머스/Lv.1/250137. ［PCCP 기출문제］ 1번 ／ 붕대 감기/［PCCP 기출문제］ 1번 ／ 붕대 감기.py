def solution(bandage, health, attacks):
    answer = 0
    max_time = attacks[-1][0]
    max_health = health
    cnt = 0
    attack_dic = {} 
    for i in attacks:
        attack_dic[i[0]] = i[1]
        
    for i in range(max_time+1):
        if i in attack_dic:
            health -= attack_dic[i]
            cnt = 0
            if health <= 0:
                return -1
        else:
            cnt += 1
            if cnt == bandage[0]:
                health += bandage[2]
                health += bandage[1]
                cnt = 0
                if health > max_health:
                    health = max_health
            else:
                health += bandage[1]
                if health > max_health:
                    health = max_health
                
    return health