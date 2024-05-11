import math
def solution(b, y):

    return [((b+4)/2 + math.sqrt(((b+4)/2)**2-4*(b+y)))/2 , ((b+4)/2 - math.sqrt(((b+4)/2)**2-4*(b+y)))/2]