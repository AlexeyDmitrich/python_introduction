year = int (input("Введите год \n"))

def is_vis (year):
     if ((year%4==0)): #and (not(year%100==0))) or year%400==0 ):
         return True
     else:
         return False

if is_vis(year):
    print ("Високосный")
else:
    print ("Не високосный")