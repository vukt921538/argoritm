s = input('s : ')
result = s.find('PM')
result2 = s.find('AM')
new_arr = []
if result2 == -1 and result == -1:
    print('Input ERROR !')
else:
    ar = s.strip().split(':')
    # print(ar)
    check1 = ar[2].find('PM')
    check2 = ar[2].find('AM')
    if check1 != -1:
        ar[0] = int(ar[0]) + 12
        item = ar[2].translate({ord(i): None for i in 'PM'}) #Remove 'PM'
        new_arr.append(str(ar[0]))
        new_arr.append(ar[1])
        new_arr.append(item)
    elif check2 != -1:
        item = ar[2].translate({ord(i): None for i in 'AM'})
        new_arr.append(ar[0])
        new_arr.append(ar[1])
        new_arr.append(item)
if new_arr[0] == 24:
    new_arr[0] = '00'
print(':'.join(new_arr))