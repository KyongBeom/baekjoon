A, B = map(int,input().split())

if B > 44:
    print(A,B-45)
elif B < 45:
    if A == 0:
        print(23,B+15)
    else:
        print(A-1,B+15)