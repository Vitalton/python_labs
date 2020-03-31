a_list = [10, 2.6, False, 'lab-work-3', [2, 5, 8]]
print("Наш список: ", a_list)
from collections.abc import Collection, Sized, Iterable, Iterator, Container
for i in a_list:
    print(i, ":\n", type(i))
    if (isinstance(i, Collection) or isinstance(i, Sized) or isinstance(i, Iterable) or isinstance(i, Iterator) or isinstance(i, Iterator)):
        print(" АВС-класс")
print("\n")
a_list.extend('Squirrel')
print("Наш список после extend(): ", a_list)
a_list.pop(3)
print("Наш список после pop(): ", a_list)
a_list[2] = True
print("Наш список после [i]: ", a_list)
print("\n")
s = "национальный_технический_университет_харьковский_политехнический_институт"
b_list = s.split("_")
print("Список из слов разделённой строки:", b_list, "\n")
print("Длина каждого слова в списке:")
for i in b_list:
    print(i, ": ", len(i), " символов(-а)")
def max_str_in_list(list):
    maxi = ""
    for i in b_list:
        if (len(i) > len(maxi)):
            maxi = i
    return maxi
print("\nСамое длинное слово в списке: ", max_str_in_list(b_list))
