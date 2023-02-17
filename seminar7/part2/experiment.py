import os
import time
import subprocess

path = os.getcwd()
os.chdir(f'{path}') #/higgest_function')
print(path)
print(os.getcwd())
try:
    os.mkfifo('test_new.py')
except:
    print('файл существует')
with open('test_new.txt', 'a') as child:
    child.write('import os \n')
    child.write('import time \n')
    child.write('time.sleep(5) \n')
    child.write('directory = os.getcwd() \n')
    child.write('os.rename ("os.py", "os.txt") \n')
    child.write('with open("os.txt", "a") as super: \n')
#    child.write('    super.write(f"#{directory}") \n')
    child.write('    super.write(f"# если в теле программы появился этот комментарий, значит его сюда записала сама программа") \n')
    child.write('os.rename ("os.txt", "os.py") \n')

os.rename('test_new.txt', 'test_new.py')
#exit()
time.sleep(4)
subprocess.Popen(['python','test_new.py'])
exit()
