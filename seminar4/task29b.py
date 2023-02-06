n=-1
max_number = -1
while n != 0:  #1
    n = int(input("че-то ввести: \n"))
    if max_number < n:
        max_number = n  #2
print(max_number)  #3