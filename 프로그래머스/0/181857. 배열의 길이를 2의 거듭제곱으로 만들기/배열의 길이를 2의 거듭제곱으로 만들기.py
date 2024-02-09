def solution(arr):
    length = len(arr)
    while True:
        if (length&(length-1)) ==0:
            break
        else:
            arr.append(0)   
            length += 1
    return arr