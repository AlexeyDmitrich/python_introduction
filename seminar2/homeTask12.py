# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
#  школьница. Петя помогает Кате по математике. Он задумывает два
#  натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
#  этого Петя делает две подсказки. Он называет сумму этих чисел S и их
#  произведение P. Помогите Кате отгадать задуманные Петей числа


s_sum = int(input("Введите сумму двух чисел\n")) 
p_prod = int(input("Введите произведение этих чисел\n"))

x_all = []
y_all = []
for num in range (1000):
    x_all.append(num+1)
    y_all.append(num+1)
# print(x_all)

def search_nums (set_x, set_y):
    for num_x in x_all:
        for num_y in y_all:
            if ((num_x+num_y == s_sum) and (num_x*num_y == p_prod)):
                return num_x, num_y
             
#    print("Такого решения нет")

def search_nums_2 (set_x):
    for num_x in x_all:
        if (p_prod/num_x == s_sum-num_x):
            return num_x, s_sum-num_x

#    print("Такого решения нет")

try:
    x, y = search_nums(x_all, y_all)
    print("v1: ", x, y)
except:
    print("V1: Такого решения нет")

try:
    m, n = search_nums_2(x_all)
    print("v2: ", m, n)
except:
    print("V2: Такого решения нет")
