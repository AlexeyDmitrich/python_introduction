# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transormed_values = list(map(transformation, values))

# res = list(filter(lambda x : x values == transormed_values, values)) 

values = [1, 23, 42, 'asdfg'] #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
trasformation = lambda x: x
transformed_values = list(map(trasformation, values))
transformed_values[0] += 1

res = list(filter(lambda x: x[0] == x[1], zip(values, transformed_values)))
print('ok') if res == transformed_values else print('fail')
print(values)
print(transformed_values)
print(res)