# RLE aaaaabbbb = 5a4b

users_string = input("Введите строку для кодирования/декодирования:\n")

def string_to_list (input_string):
    blocks = [ [] ]
    blocks[0].append(input_string[0])
    j=0
    for i in range(1, len(input_string)):
        while (j < len(input_string)):
#            print(f"i: {i}, {input_string[i]}; \nj: {j}, {blocks[j]}")
            if input_string[i] == input_string[i-1]:
                blocks[j].append(input_string[i])
            else:
                blocks.append([input_string[i]])
                j+=1
            break
    print(blocks)

string_to_list(users_string)
