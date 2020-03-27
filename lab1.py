print("Функция & : ")
help("&")

def checker_1(number_bin):
    if (len(number_bin) == 8):
        is8 = True
    else:
        is8 = False
    return is8

first_dec = int(input("Введите первое число в 10-ричной системе счисления: "))
second_hex = input("Введите второе число в 16-ричной системе счисления: ")
second_dec = int(second_hex, 16)
print("Второе число в 10-ричной системе счисления: ", second_dec)
result_dec = int(first_dec / second_dec)
print("Результат операции в 10-ричной системе счисления: ", result_dec)
result_oct = oct(result_dec)
print("Результат операции в 8-ричной системе счисления: ", result_oct, "\n")

third_bin = input("Введите число в 2-чной системе счисления длинной 8 байт : ")
while (checker_1(third_bin) == False):
    print("Длина должна быть 8 байтов")
    third_bin = input("Введите число в 2-чной системе счисления длинной 8 байт : ")

fourth_bin = input("Введите число в 2-чной системе счисления длинной 8 байт : ")
while (checker_1(fourth_bin) == False):
    print("Длина байтов должна быть 8 байтов")
    fourth_bin = input("Введите число в 2-чной системе счисления длинной 8 байт : ")

third = int(third_bin, 2)
fourth = int(fourth_bin, 2)
print("Первое число до сдвига :", third)
print("Первое число после сдвига :", third>>2)
print("Второе число до сдвига :", fourth)
print("Второе число после сдвига :", fourth>>2)
