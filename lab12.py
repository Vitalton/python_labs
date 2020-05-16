from HistoryPerson import HistoryPerson
class A(HistoryPerson):
    def __init__(self, surname):
        self.surname  = surname
a = A("issak")
a.name = "newton"
print(a.surname + "  " + a.name)
