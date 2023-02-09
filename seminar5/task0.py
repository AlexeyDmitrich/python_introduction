#посчитать сумму всех чисел от 1 до N, N вводит пользователь

def summa(n):
    sum=0
    for i in range(n+1):
       sum+=i
    return sum

def summa2(n):
    sum=0
    while True:
       if n==0: 
          break
       sum+=n
       n-=1
    return sum

def summa_rec(n):
    if n==0: 
        return 0
    return n + summa_rec(n-1)

# 5 + (4 + (3 + (2 + (1 + 0 ))))

N = int(input("Введите целое число "))
# sum  = 0
# for i in range(N+1):
#     sum+=i
# print(sum)
print(summa(N))
print(summa2(N))
print(summa_rec(N))