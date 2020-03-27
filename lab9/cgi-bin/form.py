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
