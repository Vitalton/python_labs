a_tuple = 10, 2.6, False,  [2, 5, 8]
print("Кортеж: ", a_tuple)
from collections.abc import Container, Iterator, Iterable, Sequence, MutableSequence
if (isinstance(a_tuple, Container)):
    print("Контейнер")
if (isinstance(a_tuple, Iterator)):
    print("Итератор")
if (isinstance(a_tuple, Iterable)):
    print("Итерабельный объект")
if (isinstance(a_tuple, Sequence)):
    print("Последовательность")
if (isinstance(a_tuple, MutableSequence)):
    print("Изменяемая последовательность")
a_tuple = list(a_tuple)
a_tuple[1] = 7.958
a_tuple = tuple(a_tuple)
print(a_tuple)
a_range = range(-7,21,3)
print(list(a_range))
