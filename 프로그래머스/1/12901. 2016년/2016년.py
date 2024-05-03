def solution(a, b):
    sol = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    check = sum(month[:a-1])
    check += b
    answer = sol[check % 7-1]
    
    return answer