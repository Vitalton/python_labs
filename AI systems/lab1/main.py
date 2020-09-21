import math

# Обьекты
first = [0 ,0]
second = [0 ,0]
print("Введите координаты первого объекта: ")
first[0],first[1] = map(int,input().split())
print("Введите координаты второго объекта: ")
second[0],second[1] = map(int,input().split())
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
    return round(rezult, 4)

def Minkowski(first, second):
    temp = 0
    for i in range(len(first)):
        temp += math.pow((first[i] - second[i]), 4)
    rezult = math.pow(temp, 1/4)
    return round(rezult, 4)

def WeightingFactor(first, second):
    temp = 0
    for i in range(len(first)):
        temp += N * (math.pow((first[i] - second[i]), 2))
    rezult = math.sqrt(temp)
    return round(rezult, 4)

def Canberra(first, second):
    rezult = 0
    for i in range(len(first)):
        numerator = abs(first[i] - second[i])
        denominator = abs(first[i] + second[i])
        rezult += (numerator / denominator)
    return round(rezult, 4)

def BetweenVectors(first, second):
    try:
        temp = 0
        rezult = 0
        for i in range(len(first)):
            temp += math.pow((second[i] - first[i]), 2)
        for i in range(len(first)):
            rezult += math.acos((first[i] * second[i]) / math.sqrt(temp))
        print(round(rezult, 4))
    except ZeroDivisionError:
        print('Деление на 0!')
    except ValueError:
        print('Значение выражения вышло за пределы интервала [-1; 1]')

def RusselAndRao():
    rezult = a / (a + b + g + h)
    return round(rezult, 4)

def JokardAndNeedman():
    try:
        rezult = a / (a + g + h)
        return round(rezult, 4)
    except ZeroDivisionError:
        print('Деление на 0!')

def Dice():
    try:
        rezult = a / (2 * a + g + h)
        return round(rezult, 4)
    except ZeroDivisionError:
        print('Деление на 0!')

def SokalAndSnif():
    try:
        rezult = a / (a + 2 * (g + h))
        return round(rezult, 4)
    except ZeroDivisionError:
        print('Деление на 0!')

print("\nРасстояния по Евклиду: ", Euclid(first, second))
print("Расстояния по Минковскому: ", Minkowski(first, second))
print("С учётом весового коэффициента: ", WeightingFactor(first, second))
print("Расстояния по Камберру: ", Canberra(first, second))
print("Распознавание по углу между векторами: ")
BetweenVectors(first, second)
print("\nНеобходимые переменные: ", "\n", "a = ", a, "\n", "b = ", b, "\n", "g = ", g, "\n", "h = ", h)
print("Функция сходства Рассела и Рао: ", RusselAndRao())
print("Функция сходства Жокара и Нидмена: ", JokardAndNeedman())
print("Функция сходства Дайса: ", Dice())
print("Функция сходства Сокаля и Снифа: ", SokalAndSnif())
input("\n\n\nНажмите любую клавишу...")