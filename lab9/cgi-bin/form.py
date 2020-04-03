#!/usr/bin/env python3
import cgi
import sys
import codecs
import re
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
data1 = form.getfirst("data1")
data2 = form.getfirst("data2")
data3 = form.getfirst("data3")
literal = form.getfirst("literal")

x1 = re.search(r'гр[.]\s\w+[,]\sф\sт[:]\s\w+',data1)
if x1 :
    data1 = x1.group()
else :
    data1 = "Error"

x2 = re.search(r'\w+\s\w[.]\w[.]',data2)
if x2 :
    data2 = x2.group()
else :
    data2 = "Error"

x3 = re.search(r'ЗК\s№\s\d+',data3)
if x3 :
    data3 = x3.group()
else :
    data3 = "Error"

x4 = re.search(r'\w+\s\d+[.]\d+',literal)
if x4 :
    literal = x4.group()
else :
    literal = "Error"

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
        <meta charset="UTF-8" />
        <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>1 :  {}</p>".format(data1))
print("<p>2 :  {}</p>".format(data2))
print("<p>3 :  {}</p>".format(data3))
print("<p>4 :  {}</p>".format(literal))


print("""</body>
        </html>""")
