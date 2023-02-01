from random import randint
x=randint(0,100)
# if x>50:
#     y=True
# else:
#     y=False
y = True if x>50 else False
print(f'сгенерировано число {x}')
print(y)

i = 0
sum = 0
while i<=x:
    sum+=i
    i+=1
print(sum)

sum2=0
for i in range(x+1):
    sum2+=i
print(sum2)

for i in 4,66.77,88,True,"привет":
    print(i)

sp=["dsfsdf",88,55,True]

for k,v in enumerate(sp):
    if v==55:
        continue
    print(k,v)