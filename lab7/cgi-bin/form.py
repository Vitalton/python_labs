#!/usr/bin/env python3

import cgi
import numpy as np
print("Content-Type: text/html")
print()

list = np.random.randint(-33, 44, 16)
print("Массив случайных чисел: ", list, "<br>")

# GROUP 1
def func_1(list):
    rezult = 0
    for i in list:
        if (i > 0):
            rezult += i
    return rezult

# GROUP 2
def func_2(list):
    arr = []
    for i in list:
        if (i < 0):
            arr.append(i)
    rezult = max(arr)
    return rezult

# GROUP 3
def func_3(list):
    return sorted(list, key=abs)


form = cgi.parse(keep_blank_values=1)
if "check1" in form or "check2" in form or "check3" in form:
    if "check1" in form:
        print("Сумма положительных чисел: ", func_1(list), "<br>")
    if "check2" in form:
        print("Максимальное число среди отрицательных чисел: ", func_2(list), "<br>")
    if "check3" in form:
        print("Сортировка чисел, взятых по абсолютной величине: ", func_3(list), "<br>")
