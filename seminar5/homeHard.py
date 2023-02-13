# задача калькулятор необязательная.
# Решать только через рекурсию!. Пользоваться встроенными функциями вычисления таких выражений нельзя, если только для проверки вашего алгоритма.
# на вход подается строка из операторов / * + - и целых чисел. Надо посчитать результат введенного выражения.
# Например,
# на входе
# 1+9/3*7-4
# на выходе
# 18

users_input = input("Введите выражение")
expressions = []
splitter_list = ["-", "+", "*", "/"]
iterator=0
def split_by_priority (users_string, iterator=0, splitter=splitter_list[iterator], expressions_list=[]):
    if str(users_string).find(splitter) >= 0:
        expressions_list.append(users_string.split(splitter)) 
        return split_by_priority (expressions_list, iterator+1, splitter[iterator], expressions_list[iterator])
    return expressions_list

print (split_by_priority(users_input))

exit()
nums=[]
operations=[]
def parce_math (expression, nums, operations):
    if len(expression) == 0:
        return
    try:
        if type(int(expression[0])) == int:
            nums.append(expression[0])
    except:
        operations.append(expression[0])
    return parce_math (expression[1:], nums, operations)

parce_math(users_input, nums, operations)
print(f"Ввод: {users_input},\nчисла: {nums},\nоперанды: {operations}")
