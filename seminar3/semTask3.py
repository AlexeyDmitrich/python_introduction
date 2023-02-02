# Напишите программу для печати всех уникальных
# значений в словаре.


input_nums = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

lst = set()
for dict in input_nums:
    for v in dict.values():
        lst.add(v.strip())

print(lst)
