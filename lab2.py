s1 = "Молчанов Виталий Владимирович"
print("Первая строка:\n", s1)
s1 = s1[4:]
print("Первая строка после среза:\n", s1)
s2 = "КИТ-117Д"
print("Вторая строка:\n", s2)
s3 = s1 + s2
print("Сформированная третья строка:\n", s3, "\n")
print("Метод count('и'): ", s3.count("и"))       # возвращает число встретившихся подстрок в строке
print("Метод isalpha(): ", s3.isalpha())         # возвращает True, если содержит хотя бы один символ и все ее символы являются буквами, иначе возвращает False
print("Метод rindex('и'): ", s3.rindex("и"))     # возвращает индекс последнего совпадения строки T в строке S
print("Метод rfind('КИТ'): ", s3.rfind("КИТ"), "\n")   # возвращает начальный индекс последнего вхождения T
count_num = 0
one = int(input("В каком формате будет результат выражения 6 / 2 ?  1) 3    2) 3.0      :"))
two = int(input("Что выведет функция 'education'.isalpha()?  1) False    2) True      :"))
three = int(input("Чему равно логическое значение True ?  1) 0    2) 1      :"))
four = int(input("n=4. Чему равно значение функции n.bit_length() ?  1) 4    2) 3    2) 5      :"))
five = int(input("При каком условии оператор if выполняет свои действия ?  1) False    2) True      :"))
if one == 2:
    count_num = count_num + 1
if two == 2:
    count_num = count_num + 1
if three == 2:
    count_num = count_num + 1
if four == 1:
    count_num = count_num + 1
if five == 2:
    count_num = count_num + 1
print(f"Студент Молчанов набрал {count_num} баллов!")
