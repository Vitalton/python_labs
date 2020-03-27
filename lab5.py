a_set = set([2, 7.56, "НТУ ХПИ", 5.25, "КИТ", 2.5, 105])
print("Наше первое множество: ", a_set)

a_set.update([85, 7.56, 10, 5.25])
print("\nИзменённое первое множество: ", a_set)
a_set.remove(105)
print("\nИзменённое первое множество: ", a_set)

it_ob = ("КИТ", 10, 7.57)
b_set = set(it_ob)
print("\nНаше второе множество: ", b_set)

c_set = a_set.intersection(b_set)
print("\nРезультат операции 'intersection': ", c_set)

a_dict = {"География": 10, "Математика": 12, "Физика": 11}
print("\nНаш словарь: ", a_dict)

print("\nРезультат операции 'items': ", a_dict.items())
print("\nРезультат операции 'popitem': ", a_dict.popitem())
b_dict = { 'figure' : 'circle' , 'color' : 'green' }
a_dict.update(b_dict)
print("\nРезультат операции 'update[dict2]': ", a_dict)
