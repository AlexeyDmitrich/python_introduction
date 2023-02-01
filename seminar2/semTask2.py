num = int(input(': '))
first = 0
second = 1
counter = 2
while second <= num:
    if second == num:
        print(counter)
        break
    first, second = second, first + second
    counter+=1
else:
    print(-1)