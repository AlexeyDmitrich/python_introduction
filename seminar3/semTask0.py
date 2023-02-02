# sp = []
# sp.append(1234)
# sp.extend([888,True,"Привет"])
# sp.insert(0,'Начало')
# sp2 = [1111,7777]
# sp = sp + sp2
# a = sp.pop()
# sp.remove("Привет")
# #del sp[0]
# print(sp)
# print(a)

lst = [ i for i in range(11) if i%2==0]
print(lst)
for i,v in enumerate(lst):
    print(i,v)

# sp = [0] * 10
# print(sp)
# print(len(sp))

kort = (1,5,8,9)
print(kort[0])
#kort[0]=888

slov = {"Иван":8756155, "Сергей":[564654654,4564646465]}
print(slov['Иван'])
slov['Федор'] = 56465464
print(slov.keys())
print(slov.values())
for k,v in slov.items():
    print(k,v)