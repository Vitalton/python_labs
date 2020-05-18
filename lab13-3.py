from tkinter import *


class Task(Frame):
    ''' Использование флажков '''
    def __init__(self, master):
        super(Task, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        ''' Создает шесть флажка '''
        # метка-описание
        Label(self,text = 'Работа с цыфрами', font = 'arial 13', fg = 'blue').\
            grid(row=0, column=0,sticky=W)
        # метка-инструкция
        Label(self,text = 'Выберите нужные вам цыфры:', font = 'arial 11', fg = 'blue').\
            grid(row=1,column=0, sticky=W)
        # флажок 'буква - 1'
        self.likes_letter1=BooleanVar()
        Checkbutton(self,text='Г',variable = self.likes_letter1, command = self.update_text).\
            grid(row=2, column=0,sticky=W)
        # флажок 'буква - 2'
        self.likes_letter2=BooleanVar()
        Checkbutton(self,text = 'а', variable = self.likes_letter2, command = self.update_text
        ).grid(row=3, column=0,sticky=W)
        # флажок 'буква - 3'
        self.likes_letter3=BooleanVar()
        Checkbutton(self,text = 'м', variable = self.likes_letter3, command = self.update_text).\
            grid(row=4, column=0,sticky=W)
        # флажок 'Буква - 4 '
        self.likes_letter4=BooleanVar()
        Checkbutton(self,text = 'л', variable = self.likes_letter4, command = self.update_text
        ).grid(row=5, column=0, sticky=W)  # флажок 'Буква - 5 '
        self.likes_letter5 = BooleanVar()
        Checkbutton(self,text='е', variable=self.likes_letter5, command=self.update_text).\
            grid(row=6, column=0, sticky=W)
        # флажок 'Буква - 6 '
        self.likes_letter6 = BooleanVar()
        Checkbutton(self,text='т', variable=self.likes_letter6, command=self.update_text).\
            grid(row=7, column=0, sticky=W)
        # текстовая область с результатом
        self.results_txt = Text(self, fg='black', font='14', width=50, height=5, wrap=WORD)
        self.results_txt.grid(row=8, column=0, columnspan=3)

    def update_text(self):
        likes = ""
        if self.likes_letter1.get(): likes += 'Г'
        if self.likes_letter2.get(): likes += 'а'
        if self.likes_letter3.get(): likes += 'м'
        if self.likes_letter4.get(): likes += 'л'
        if self.likes_letter5.get(): likes += 'е'
        if self.likes_letter6.get(): likes += 'т'
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)

screen = Tk()
screen.title('Использование флажков')
screen.geometry('465x300')
app4 = Task(screen)
screen.mainloop()
