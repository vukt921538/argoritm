import math
def DiagonalDifference():
    n = int(input())
    matrix = []
    for i in range(n):
        arr = [int(arr) for arr in input().split()]
        matrix.append(arr)
    # print(matrix)
    # print matrix
    # for i in range(n):
    #     for j in range(n):
    #         print(matrix[i][j], end=' ')
    #     print() #breakline
    
    # Tổng đường chéo chính
    sum = 0
    sum2 = 0
    for i in range(n):
        sum = sum + matrix[i][i]
    # Tổng đường chéo phụ
    for i in range(n):
        sum2 = sum2 + matrix[i][n-1-i]
    x = abs(sum - sum2)
    print(x)
DiagonalDifference()
