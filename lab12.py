from HistoryPerson import HistoryPerson

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


a = Add_info("newton", "issak", "phisic")
a.getInfo()
a.setYear(1674)
a.getInfo()

