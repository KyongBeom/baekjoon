import re
def solution(myStr):
    sol = re.sub("[a-c]", " ", myStr).split()
    if len(sol) > 0:
        return sol
    else:
        return ["EMPTY"]
    