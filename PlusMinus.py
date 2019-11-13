arr = list(map(int, input().strip().split()))
count_positive = 0
count_zeros = 0
count_negative = 0
for item in arr:
    if item > 0:
        count_positive += 1
    elif item < 0:
        count_negative += 1
    elif item == 0:
        count_zeros += 1

print(count_positive/len(arr))
print(count_negative/len(arr))
print(count_zeros/len(arr))