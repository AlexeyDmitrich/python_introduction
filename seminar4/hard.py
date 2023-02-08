# RLE aaaaabbbb = 5a4b
# RLE aaaaabbbb = 5a4b

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
#    for block in blocks:
#        print(block)
    return blocks

def code (list_of_blocks):
    code_list = []
    for block in list_of_blocks:
        if len(block) == 1:
            sector = block[0]
        else:
            sector = str(len(block))+block[0]
        code_list.append(sector)
#    print (code_list)
    return code_list

def list_to_string (formated_list):
    res = ''
    for code in formated_list:
        res += f"{code}"
#    print (res)
    return res

def full_code (stdin):
    blocks = string_to_list(stdin)
    code_list = code (blocks)
    pure_code = list_to_string (code_list)
    return pure_code

users_string = input("Введите строку для кодирования/декодирования:\n")
print (full_code(users_string))

'''
test_string = input("Введите строку для декодирования:\n")

def pack_str_to_lst (lst_str):
    depack_arr = []
    for char in range(len(lst_str)):
        try:
            if type(int(lst_str[char])) == int:
                i=1
                ran=1
                val=int(lst_str[char])
                try:
                    while (type(int(lst_str[char+i])) == int):
                        val = val*10+int(lst_str[char+i])
                        i+=1
                        ran+=1                        
                except:
                    depack_arr.append(str(val * lst_str[char+ran]))
                    char+=ran
        except:
            if char > 0:
                try:
                    if type(int(lst_str[char-1])) != int:
                        depack_arr.append(lst_str[char])
                except:
                    depack_arr.append(lst_str[char])
            else:
                depack_arr.append(lst_str[char])
        print (depack_arr)
    return depack_arr
print (pack_str_to_lst(test_string))
'''
