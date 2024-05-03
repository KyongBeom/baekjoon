def solution(nums):
    check = len(set(nums))
    return min(check, len(nums)/2)