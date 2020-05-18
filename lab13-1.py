from tkinter import *

def Fibonacci(clicks):
    list_Fib = [1]
    i = 1
    while i < clicks:
        if len(list_Fib) < 2:
            list_Fib.append(i)
            i += 1
        else:
            list_Fib.append(list_Fib[-1] + list_Fib[-2])
            i += 1
    return list_Fib
class Task(Frame):
    ''' Описание рамки с кнопкой, подсчитывающей события '''
    def __init__(self, master):
         super().__init__(master)
         self.grid()
         self.btn_clicks=0
         self.create_widgets()
    def create_widgets(self):
         ''' Создает кнопку с обработкой событий '''
         self.btn=Button(text='Число щелчков: 0',
         command=self.count,
         width='116',
         height='21',
         bg='#ff0',
         font='Consolas 15',
         fg='blue',
         activebackground='#ff0',
         activeforeground='blue')
         self.btn.grid()
    def count(self):
        self.btn_clicks += 1
        start = 0
        end = 1
        i = 1
        while i == self.btn_clicks:
            self.rezult = start + end
            print(self.rezult)
            start = end
            end = self.rezult
            i += 1
        self.btn['text'] = 'Число щелчков: ' + str(self.btn_clicks) + "\n" + str(Fibonacci(self.btn_clicks))

screen = Tk()
screen.geometry("1280x500")
screen.title("Кол-во нажатий и ряд Фибоначчи")
app = Task(screen)
screen.mainloop()