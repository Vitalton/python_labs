import random
class HistoryPerson():
    '''АТРИБУТ  "Только для чтения"'''
    __character = "Настойчивость"

    '''СПЕЦИАЛЬНЫЕ МЕТОДЫ'''
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
        self.year_birth = random.randint(1580, 1630)
        self.year_death = random.randint(1630, 1680)
        if (self.year_birth - self.year_death) > 30:
            self.year_birth -= 15
            self.year_death += 15
    def __str__(self):
        return self.name + " - это историческая личность, которая внесла большой вклад в развитие науки"
    def __del__(self):
        print("Экземпляр удалён!")

    '''СТАТИЧЕСКИЙ МЕТОД'''
    @staticmethod
    def status(self):
        print("Инфо о исторической личности:")
        print("Имя:", self.name)

    '''ЗАКРЫТЫЙ МЕТОД'''
    def __privateMethod(self):
        print("Эти данные недоступны пользователю!")

    '''МЕТОД ЭКЗЕМПЛЯРА КЛАССА'''
    def setYear(self, year):
        if year >= 1580 and year <= 1680:
            return year
        else:
            print("Введено некорректное значение!")