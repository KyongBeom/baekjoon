while True:
    A,B = input().split()
    A = int(A)
    B = int(B)
    if A == B == 0:
        break
    if A > B :
        print("Yes")
    elif A<=B:
        print("No")

