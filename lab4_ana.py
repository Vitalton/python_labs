WORDS=('компьютер',
'питон' ,
'сервер' ,
'клиент' ,
'браузер' ,
'протокол' ,
'программа' ,
'процессор' ,
'контекст' )
from random import seed,choice,randrange

def hint_out():
    lenght = len(correct) - 1
    if hint == 3 :
        print(hint_word[len(correct) - 1:])
    if hint == 2 :
        print(hint_word[len(correct) - 2:])
    if hint == 1 :
        print(hint_word[len(correct) - 3:])
    if hint != 1 and hint != 2 and hint != 3 :
        print("У Вас больше нет подсказок")

seed()
word = choice(WORDS)
hint_word = str(word)
correct=word
ana=""
hint = 3
while word:
    pos=randrange(len(word))
    ana+=word[pos]
    word=word[:pos]+word[pos+1:]
print('''
          Игра "АНАГРАММА"
   Для выхода - нажмите клавишу Enter''')
print('\nЭто анаграмма: ', ana.upper())
print("У Вас есть", hint,"подсказки. Для использования напишите : подсказка")
ans = input("Найди исходное слово:  ").casefold()
while ans != correct and ans != "" :
    if (ans == "подсказка") :
        hint_out()
        hint -= 1
        print("У Вас осталось", hint, "подсказка(-ок)")
        ans = input("Ваш ответ :").casefold()
    else :
        print("""
        Ответ неверный
        """)
        ans = input("Попробуй еще раз: ").casefold()
if ans == correct :
      print("""
      Молодец!
      """)
print("Спасибо за игру")
input()
