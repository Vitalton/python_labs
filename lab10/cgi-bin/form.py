#!/usr/bin/env python3

import cgi
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# ПОЛУЧЕНИЕ ДАННЫХ ИЗ ФОРМЫ
data = cgi.FieldStorage()
name = data.getfirst("name")
answer1 = data.getfirst("answer1")
answer2 = data.getfirst("answer2")
answer3 = data.getfirst("answer3")
answer4 = data.getfirst("answer4")

# ФОРМИРОВАНИЕ И ПРОВЕРКА ШАБЛОНОВ
def check_results(answer1, answer2, answer3, answer4):
    print("<p>Ответы пользователя:</p><br>")
    print("<p>1): ", answer1, "</p><br>")
    print("<p>2): ", answer2, "</p><br>")
    print("<p>3): ", answer3, "</p><br>")
    print("<p>4): ", answer4, "</p><br>")
    count = 0
    if answer1 == "3":
        count += 1
    if answer2 == "1":
        count += 1
    if answer3 == "2":
        count += 1
    if answer4 == "2":
        count += 1
    if count > 0:
        print("<p>Правильные ответы:</p><br>")
        if answer1 == "3":
            print("<p>1): ", answer1, "</p><br>")
        if answer2 == "1":
            print("<p>2): ", answer2, "</p><br>")
        if answer3 == "2":
            print("<p>3): ", answer3, "</p><br>")
        if answer4 == "2":
            print("<p>4): ", answer4, "</p><br>")


# ВЫВОД РЕЗУЛЬТАТА ПРОВЕРКИ НА ЭКРАН
print("Content-type: text/html\n")
print("""<!DOCTYPE html>
        <html lang="ru">
        <head>
        <meta charset="UTF-8">
        <title>Lab10</title>
        <link href="https://fonts.googleapis.com/css?family=Pacifico&display=swap&subset=cyrillic,cyrillic-ext" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Montserrat:500,600,700,800,900&display=swap&subset=cyrillic,cyrillic-ext" rel="stylesheet">
        <style>
            body {
                background-image: linear-gradient(to left, #C04C8B, #264EB0);
                color: #000;
                font-family: 'Montserrat', sans-serif;
            }
            p {
                font-size: 17px;
                font-weight: 600;
            }
            #name {
                font-size: 25px;
                font-weight: 600;
            }
            #div {
                  margin-top: 50px;
                  margin-left: 38%;
                  display: inline-block;
                  justify-content: center;
                  align-items: center;
                  width: 24%;
                  border-radius: 6px;
                  background-color: white;
                  opacity: 0.7;
                  text-align: center;
                  padding: 25px;
                  box-shadow: 0 10px 16px #000;
            }
        </style>
        </head>
        <body>""")
print("<h1 align='center'>Результаты теста!</h1>")
print("<p id='name'>Фамилия:", name, "</p><br>")
check_results(answer1,answer2,answer3,answer4)
print("""</body>
        </html>""")
