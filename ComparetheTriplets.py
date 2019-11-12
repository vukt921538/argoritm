def compareTriplets():
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    a_point = 0
    b_point = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_point += 1
        elif a[i] < b[i]:
            b_point += 1
    print(a_point, b_point)
compareTriplets()
