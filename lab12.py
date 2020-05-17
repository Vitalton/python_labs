import random
from HistoryPerson import HistoryPerson

# КЛАСС-НАСЛЕДНИК
class Add_info(HistoryPerson):
    def __init__(self, surname, name, industry):
        super().__init__(surname, industry)
        self.name  = name

    def setYear(self, year):
        if year >= 1580 and year <= 1630:
            self.year_birth = year
        if year >= 1630 and year <= 1680:
            self.year_death = year
        else:
            print("Введено некорректное значение!")
    def age(self):
        return self.year_death - self.year_birth
    def getInfo(self):
        print("Фамилия: ", self._HistoryPerson__surname, "\n" + "Имя: ", self.name, "\n" + "Отрасль: ",
              self.industry, "\n" + "Год рождения: ",
              self.year_birth, "\n" + "Год смерти: ",
              self.year_death, "\n" + "Возраст: ",
              self.age(), "\n")

# ПОЛЬЗОВАТЕЛЬСКИЙ КЛАСС
class Generate():
    countries = ("Великобритания", "Германия", "Франция", "Италия", "Испания", "Нидерланды")
    def gainCountry(self):
        return random.choice(self.countries)
    def gainAge(self):
        return random.randint(1, 2020)

# КЛАСС МНОЖЕСТВЕННГО НАСЛЕДОВАНИЯ
class Human(Add_info, Generate):
    def __init__(self, surname, name, industry):
        super().__init__(surname, name, industry)
        self.country = self.gainCountry()
        self.year_birth = self.gainAge()
        self.year_death = self.gainAge()
        if self.age() < 0:
            self.year_death += 2000
            if self.year_death > 2020:
                self.year_death = 2020
        if self.age() > 100:
            print("Возраст превышает среднюю макс. продолжительность жизни!\nИзмените годы жизни "
                  "вручную!")
            print("Год рождения: ",
              self.year_birth, "\n" + "Год смерти: ",
              self.year_death, "\n" + "Возраст: ",
              self.age(), "\n")
            print("1. Изменить год рождения\n2. Изменить год смерти\n3. Человек жив!")
            option = input("Введите номер операции: ")
            if option == "1":
                self.year_birth = int(input("Введите год рождения: "))
            if option == "2":
                self.year_death = int(input("Введите год смерти: "))
            if option == "3":
                self.year_death = 2020

# НАСЛЕДОВАНИЕ ОТ НЕИЗМЕНЯЕМОГО КЛАССА
class Converter(float):
    def __new__ (cls,arg):
        arg *= 3.28
        return round(arg, 2)

# КЛАСС-ПОСЛЕДОВАТЕЛЬНОСТЬ
class My_list():
    ''' Пользовательский класс, близкий к списку '''
    def __init__ (self, values = None) :
        if values is None :
            self.values = []
        else:
            self.values = values
    def __getitem__ (self, key):
        ''' Получить значение по ключу '''
        return self.values[key]
    def __setitem__ (self, key, value):
        ''' Установить значение по ключу '''
        self.values[key] = value
    def first (self):
        ''' Получить значение первого элемента '''
        return self.values[0]
    def __iter__(self):
        ''' Сделать последовательность итерабельной '''
        return iter(self.values)
    def __str__(self):
        ''' Возвратить строковое представление объекта '''
        return "Мой список: " + str(self.values)


Newton = Add_info("Ньютон", "Исаак", "Физика")
Newton.getInfo()
Newton.setYear(1674)
Newton.getInfo()

Me = Human("Молчанов", "Виталий", "Программирование")
Me.getInfo()
print("Страна рождения: ", Me.country)
print("\n")

num = int(input("Введите длину в метрах: "))
print("Длина в футах: ", Converter(num))
print("\n")

list1 = My_list([1,5,3,7,"list"])
print(list1)
print("Ваш элемент: ", list1[4])
list1[4] = 252
print("Ваш элемент: ", list1[4])
print("Первый элемент: ", list1.first())
print("Итерабельная последовательность: ")
for i in list1:
    print (i, end= ' ')
print("\n")