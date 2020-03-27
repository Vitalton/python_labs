import my_custom_module
arr = [1.9,6,3.78,3,3,56,7,8,0.8]
print("Список 1: ", arr, "\n")
def  func1(list):
    return min(list)
print("Результат 1-ой функции: ", func1(arr), "\n")
a_dict = {"Сложение": 1, "Вычитание": 2, "Умножение": 3, "Деление": 6, "Деление по модулю": 5, "Возведение в степень": 6, "Целочисленное деление": 7, "Присваивание": 6}
print("Словарь 1: ", a_dict, "\n")
def func2(dict, num):
    current_list = []
    for i in dict:
        if (dict[i] == num):
            current_list += [i]
    return current_list
print("Результат 2-ой функции: ", func2(a_dict, 6), "\n")
a_list = ["НТУ", "Факультет", [1,8,4,2,6,8], "ХПИ", [4,9,2,7]]
print("Список 2: ", a_list, "\n")
def func3(lists):
    current_list = []
    for i in lists:
        current_list.append(len(i))
    return current_list
a_list = func3(a_list)
a_list.sort(reverse = True)
print("Результат 3-ой функции с сортировкой: ", a_list, "\n")
str_code =  '''
x=5
y=x**3+1
print(y) '''
comp_code = compile(str_code, "<string>" , "exec")
print("Выполнение скомпилированного кода: ")
exec(comp_code)
print("\nРезультат функции из модуля для списка 1: ", my_custom_module.add(arr))
print("\nРезультат функции из модуля для значений словаря: ", my_custom_module.add(a_dict.values()))
