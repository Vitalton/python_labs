#!/usr/bin/env python3

import cgi
import os, os.path
import math
print("Content-Type: text/html")
print()

# ПОЛУЧЕНИЕ ДАННЫХ ИЗ ФОРМЫ
form = cgi.FieldStorage()
name_f = form.getfirst("name", "не задано")
values_f = [form.getfirst("nameDep", "не задано"), form.getfirst("course", "не задано")]
x = int(form.getfirst("x", "не задано"))

# СОЗДАНИЕ ФАЙЛОВ 'name', 'values'
os.mkdir("CGI")
name = open("CGI\\name.txt", "w")
values = open("CGI\\values.txt", "w")
name.write(name_f)
values.writelines(values_f)
name.close()
values.close()

# ЧТЕНИЕ ФАЙЛОВ 'name', 'values'
name = open("CGI\\name.txt", "r")
values = open("CGI\\values.txt", "r")
print("Размер 'name.txt': ", os.path.getsize("D:\\Education\\Python\\Python-Labs\\lab8\\CGI\\name.txt"), " байт(-а)<br>")
print("Размер 'values.txt': ", os.path.getsize("D:\\Education\\Python\\Python-Labs\\lab8\\CGI\\values.txt"), " байт(-а)<br>")
print("Содержимое файла 'values.txt': ", values.readline(), "<br>")
name.close()
values.close()

# СОЗДАНИЕ И ЧТЕНИЕ ФАЙЛА 'binary_data.dat'
bin = open("CGI\\binary_data.dat", "wb")
bin.write(bytes(range(26)))
bin.close()
bin = open("CGI\\binary_data.dat", "rb")
print("Содержимое файла 'binary_data.dat': ", bin.read(), "<br>")
bin.seek(20)
print("Содержимое 20-го байта файла 'binary_data.dat': ", bin.read(1), "<br>")
bin.seek(-12, 1)
print("Содержимое файла 'binary_data.dat' после смещения: ", bin.read(3), "<br>")

# ОБРАБОТКА ИСКЛЮЧЕНИЙ
while True:
    try:
        assert x >= 1
        if (x > 2):
            i = 2
            limit = int(math.sqrt(x))
            while i <= limit:
                if x % i == 0:
                    print(x, "составное число!")
                    quit()
                i += 1
            print(x, "простое число!")
        else:
            print(x, "простое число!")
        break
    except AssertionError:
        print ("Ошибка: деление на 0")
    except AssertionError:
        print ("Число ни сложное, ни простое")
