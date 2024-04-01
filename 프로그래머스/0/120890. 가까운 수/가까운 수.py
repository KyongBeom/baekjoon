def solution(array, n):
    array.append(n)
    array = sorted(array)
    if array.index(n) == len(array)-1:
        return array[-2]
    else:
        a = n - array[array.index(n)-1]
        b = array[array.index(n)+1] - n
        if a <= b:
            return array[array.index(n)-1]
        else:
            return array[array.index(n)+1]