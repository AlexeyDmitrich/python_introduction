str = """She sells sea shells on the sea shore The shellsthat she sells are sea shells 
I'm sure.So if she sells sea 
shells on the sea shore I'm sure that the shells are sea
shore shells"""

znaki = ['.', ',',';']

for z in znaki:
    str = str.replace(z, ' ')

print(str)

lst = set(str.lower().split()) 

print(len(lst))

exit()

s = "She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.\
    So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells"
s = s.replace('.', ' ').replace(',', ' ').replace(';', ' ')
lst = s.lower().split()
print(lst)
print(len(set(lst)))

exit()

word = input("Введите слово:")
array = []
for i in word:
    array += i.split(' ')
score = 0
many_letters = set(word)
for i in many_letters:                    
    for j in range(0,len(array)):
        if i == array[j]:
            score += 1
            if score >=2:
                array[j] = array[j] +'_'+ str(score - 1)  
    score = 0
print(" ".join(array))