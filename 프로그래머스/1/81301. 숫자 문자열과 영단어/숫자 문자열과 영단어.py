def solution(s):
    answer = ""
    check = ""
    arr = ['zero', 'one','two', 'three','four','five','six','seven','eight','nine']
    
    for i in s:
        if i.isnumeric():
            answer += i
        else:
            check += i
            if check in arr:
                answer += str(arr.index(check))
                check = ""
            
    return int(answer) 