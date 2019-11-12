def simpleArraySum():
    n = int(input())
    sum = 0
    # input multiple value:
    ar = [int(ar) for ar in input().split()]
    
    if len(ar) > n:
        print('Out of range !')
    else:
        for item in ar:
            sum = sum + item
        print(sum)
simpleArraySum()