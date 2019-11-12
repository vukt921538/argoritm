n = int(input())
char = ''
for i in range(n):
    i = '#'
    char = char + str(i)
    print(char.rjust(n, ' '))