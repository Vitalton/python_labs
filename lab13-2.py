from tkinter import *


class Task(Frame):
    ''' Рамка для работы с текстом '''
    def __init__(self, master):
        super(Task, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self["bg"] = "#ff0"
        ''' Создает 2 метки, текстовое поле, текстовую область и кнопку'''
        self.lb2 = Label(self, text='Пароль', bg='#ff0', fg='blue', font='Comfortaa 20')
        #self.lb2.grid(row=0, column=3, sticky=E)
        # текстовое поле для ввода пароля
        self.ent = Entry(self, bg='#fff', fg='blue', font='Consolas 15', justify="center",
                         width="30")
        #self.ent.grid(row=1, column=3, sticky=E)
        # создание текстовой области, куда будет помещен ответ
        self.txt2=Text(self, width=30, height=4, wrap=WORD, bg='#fff', fg='blue',
                       font = 'Consolas 15')
        #self.txt2.grid(row=4, column=1, columnspan=2)
        self.txt = Text(self,  width=30, height=4, wrap=WORD, bg='#fff', fg='blue',
                        font='Consolas 15')
        #self.txt.grid(row=4, column=3, columnspan=4)
        # кнопка отправки сообщения
        self.bt=Button(self, text = 'Подтвердить', fg = 'blue', bd = '2', font = 'Comfortaa 15',
                       command = self.reveal, activeforeground='blue')
        #self.bt.grid(row=2, column=3, sticky=E)
        self.lb2.grid(padx=15,pady=5)
        self.ent.grid(padx=15,pady=5)
        self.txt.grid(padx=15,pady=5)
        self.txt2.grid(padx=15, pady=5)
        self.bt.grid(padx=15,pady=5)
        self.txt.insert(0.0, 'Введите пароль')


    def reveal(self):
        contents = self.ent.get()  # Вы ошиблись номером
        if contents == 'password':
            self.txt.delete(0.0, END)
            message2 = 'Вы успешно вошли!'
        else:
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, 'Введите пароль')
            message2 = 'Вы ввели неправильный пароль.'
        self.txt2.delete(0.0, END)
        self.txt2.insert(0.0, message2)

screen = Tk()
screen.title('Авторизация в системе')
screen.geometry('380x400')
screen.resizable(width=False,height=False)
screen["bg"] = "#ff0"
app = Task(screen)
screen.mainloop()
