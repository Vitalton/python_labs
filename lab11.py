import random
class HistoryPerson():
    __character = "Настойчивость" # АТРИБУТ  "Только для чтения"

    # СПЕЦИАЛЬНЫЕ МЕТОДЫ
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
        self.year_birth = random.randint(1580, 1630)
        self.year_death = random.randint(1630, 1680)
        if (self.year_birth - self.year_death) > 30:
            self.year_birth -= 15
            self.year_death += 15
    def __str__(self):
        return self.name + " - это историческая личность, которая внесла большой вклад в развитие науки: "
    def __del__(self):
        print("Экземпляр удалён!")

    # СТАТИЧЕСКИЙ МЕТОД
    @staticmethod
    def status(self):
        print("Инфо о исторической личности:")
        print("Имя:", self.name)

    # ЗАКРЫТЫЙ МЕТОД
    def __privateMethod(self):
        print("Эти данные недоступны пользователю!")

    # МЕТОД ЭКЗЕМПЛЯРА КЛАССА
    def setYear(self, year):
        if year >= 1580 and year <= 1680:
            return year
        else:
            print("Введено некорректное значение!")

Newton = HistoryPerson("Ньютон", "Физика")
Newton.status(Newton)
print(Newton)
print("Год рождения: ", Newton.year_birth)
print("Год смерти: ", Newton.year_death)
Newton.year_birth = Newton.setYear(1590)
print("Год рождения: ", Newton.year_birth)
print("Черта характера: ", Newton._HistoryPerson__character)
Newton._HistoryPerson__privateMethod()
print("Отрасль: ", Newton.industry)
delattr(Newton, "industry")

print("\n")

Galilei = HistoryPerson("Галилей", "Астрономия")
Galilei.status(Galilei)
print("Год рождения: ", Galilei.year_birth)
print("Год смерти: ", Galilei.year_death)
Galilei.year_death = Galilei.setYear(1675)
print("Год смерти: ", Galilei.year_death)
print("Черта характера: ", Galilei._HistoryPerson__character)
Galilei._HistoryPerson__privateMethod()
print("Отрасль: ", Galilei.industry)
delattr(Galilei, "industry")