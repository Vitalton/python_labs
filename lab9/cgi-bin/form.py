#!/usr/bin/env python3
import cgi
import sys
import codecs
import re
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# ПОЛУЧЕНИЕ ДАННЫХ ИЗ ФОРМЫ
form = cgi.FieldStorage()
data1 = form.getfirst("data1")
data2 = form.getfirst("data2")
data3 = form.getfirst("data3")
literal = form.getfirst("literal")

# ФОРМИРОВАНИЕ И ПРОВЕРКА ШАБЛОНОВ
pattern_data1 = re.search(r"гр[.]\s\w+[,]\sф[-]т[:]\s\w+", data1)
if pattern_data1:
    data1 = pattern_data1.group()
else:
    data1 = "Error"

pattern_data2 = re.search(r"\w[.]\w[.]\s\w+", data2)
if pattern_data2:
    data2 = pattern_data2.group()
else:
    data2 = "Error"

pattern_data3 = re.search(r"ЗК\s№\s\d+", data3)
if pattern_data3:
    data3 = pattern_data3.group()
else:
    data3 = "Error"

pattern_literal = re.search(r"\w+\s\d+[.]\d+", literal)
if pattern_literal:
    literal = pattern_literal.group()
else:
    literal = "Error"

# ВЫВОД РЕЗУЛЬТАТА ПРОВЕРКИ НА ЭКРАН
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
        <meta charset="UTF-8" />
        <title>РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ</title>
        <link href="https://fonts.googleapis.com/css?family=Pacifico&display=swap&subset=cyrillic,cyrillic-ext" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Montserrat:500,600,700,800,900&display=swap&subset=cyrillic,cyrillic-ext" rel="stylesheet">
        <style>
            body {
                background-image: linear-gradient(to left, #C04C8B, #264EB0);
                color: #fff;
                font-family: 'Montserrat', sans-serif;
            }
            p {
                font-size: 25px;
                font-weight: 600;
            }
        </style>
        </head>
        <body>""")

print("<h1 align='center'>Результат обработки формы!</h1>")
print("<p>1 :  {}</p>".format(data1))
print("<p>2 :  {}</p>".format(data2))
print("<p>3 :  {}</p>".format(data3))
print("<p>4 :  {}</p>".format(literal))


print("""</body>
        </html>""")
