def make(x,y):
    while y > 0:
        x,y = y, x%y
    return x
def solution(n1, d1, n2, d2):
    answer = []
    top = n1 * d2 + n2 * d1
    bottom = d1 * d2
    max_small = make(top, bottom)
    return [top//max_small, bottom//max_small]