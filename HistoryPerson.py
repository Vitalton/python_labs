import random
class HistoryPerson():
    '''СПЕЦИАЛЬНЫЕ МЕТОДЫ'''
    def __init__(self, surname, industry):
        self.__surname = surname # АТРИБУТ "Только для чтения"
        self.industry = industry
        self.year_birth = random.randint(1580, 1630)
        self.year_death = random.randint(1630, 1680)
        if (self.year_death - self.year_birth) > 24:
            self.year_birth -= 10
            self.year_death += 10
    def __str__(self):
        return self.__surname + " - это историческая личность, которая внесла большой вклад в развитие науки"
    def __del__(self):
        print("Экземпляр удалён!")

    '''СТАТИЧЕСКИЙ МЕТОД'''
    @staticmethod
    def status(self):
        print("Инфо о исторической личности:")
        print("Фамилия:", self.__surname)

    '''ЗАКРЫТЫЙ МЕТОД'''
    def __privateMethod(self):
        print("Эти данные недоступны пользователю!")

    '''МЕТОД ЭКЗЕМПЛЯРА КЛАССА'''
    def setYear(self, year):
        if year >= 1580 and year <= 1680:
            return year
        else:
            print("Введено некорректное значение!")