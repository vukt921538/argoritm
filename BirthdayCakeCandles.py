n = int(input())
arr = list(map(int, input().rstrip().rsplit()))
print(max(arr))
count = 0
for item in arr:
    if item == max(arr):
        count += 1
print(count)
