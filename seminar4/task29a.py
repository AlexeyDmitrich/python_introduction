n = int(input("че-то ввести: \n"))
max_number = n #1
while n != 0:
    n = int(input())
    if max_number < n:  #2
        max_number = n 
print(max_number)