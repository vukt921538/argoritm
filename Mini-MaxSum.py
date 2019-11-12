arr = list(map(int, input().rstrip().split()))
arr.sort()
print(arr)
sum = 0
sum2 = 0
for i in range(1, len(arr)):
    sum = sum + arr[i]
for i in range(len(arr)-1):
    sum2 = sum2 + arr[i]
print(sum2, sum)