class HistoryPerson():
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
    def __str__(self):
        return self.name + " - это историческая личность, которая внесла большой вклад в развитие отрасли: " + self.industry
    def __del__(self):
        print("Экземпляр удалён!")
    def getting(self):
        print("Имя:", self.name + "\nОтрасль: ", self.industry)

a = HistoryPerson("Репин", "изобразительное исскувство")
a.getting()
print(a)
del(a)