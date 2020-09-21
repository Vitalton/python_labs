import math

# Обьекты
first = []
second = []
print("Введите координаты первого объекта")
for i in range(2):
    first.insert(i, int(input("Введите координату: ")))
print("\nВведите координаты второго объекта")
for i in range(2):
    second.insert(i, int(input("Введите координату: ")))
# first = [5, 6] # Si
# second = [1, 2] # Xj
N = 5 # Весовой коэффициент для формулы 1.5
a = 0
b = 0
g = 0
h = 0
for i in range(len(first)):
    a += first[i] * second[i]
    b += (1 - first[i]) * (1 - second[i])
    g += first[i] * (1 - second[i])
    h += second[i] * (1 - first[i])

print('\nКоординаты 1-го обьекта: ', first)
print('Координаты 2-го обьекта: ', second)

# Функции
def Euclid(first, second):
    temp = 0
    for i in range(len(first)):
        temp += math.pow((first[i] - second[i]), 2)
    rezult = math.sqrt(temp)
    return rezult

def Minkowski(first, second):
    temp = 0
    for i in range(len(first)):
        temp += math.pow((first[i] - second[i]), 4)
    rezult = math.pow(temp, 1/4)
    return rezult

def WeightingFactor(first, second):
    temp = 0
    for i in range(len(first)):
        temp += N * (math.pow((first[i] - second[i]), 2))
    rezult = math.sqrt(temp)
    return rezult

def Canberra(first, second):
    rezult = 0
    for i in range(len(first)):
        numerator = abs(first[i] - second[i])
        denominator = abs(first[i] + second[i])
        rezult += (numerator / denominator)
    return rezult

def BetweenVectors(first, second):
    rezult = 0
    for i in range(len(first)):
        rezult += math.acos((first[i] * second[i]) / (abs(first[i]) * abs(second[i])))
    return rezult

def RusselAndRao():
    rezult = a / (a + b + g + h)
    return rezult

def JokardAndNeedman():
    rezult = a / (a + g + h)
    return rezult

def Dice():
    rezult = a / (2 * a + g + h)
    return rezult

def SokalAndSnif():
    rezult = a / (a + 2 * (g + h))
    return rezult

print("\nРасстояния по Евклиду: ", Euclid(first, second))
print("Расстояния по Минковскому: ", Minkowski(first, second))
print("С учётом весового коэффициента: ", WeightingFactor(first, second))
print("Расстояния по Камберру: ", Canberra(first, second))
print("Распознавание по углу между векторами: ", BetweenVectors(first, second))
print("\nНеобходимые переменные: ", "\n", "a = ", a, "\n", "b = ", b, "\n", "g = ", g, "\n", "h = ", h)
print("Функция сходства Рассела и Рао: ", RusselAndRao())
print("Функция сходства Жокара и Нидмена: ", JokardAndNeedman())
print("Функция сходства Дайса: ", Dice())
print("Функция сходства Сокаля и Снифа: ", SokalAndSnif())
input("\n\n\nНажмите любую клавишу...")