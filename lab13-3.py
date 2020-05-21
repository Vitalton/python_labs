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
        Label(self,text = 'Работа с цыфрами', font = 'Comfortaa 20', fg = 'blue').\
            grid(row=0, column=0,sticky=W)

        # метка-инструкция
        Label(self,text = 'Выберите нужные вам цыфры:', font = 'Comfortaa 16', fg = 'blue').\
            grid(row=1,column=0, sticky=W)

        # флажок 'буква - 1'
        self.number1=BooleanVar()
        Checkbutton(self,text='1',variable = self.number1, command = self.sum).\
            grid(row=2, column=0,sticky=W)

        # флажок 'буква - 2'
        self.number2=BooleanVar()
        Checkbutton(self,text = '2', variable = self.number2, command = self.sum).\
            grid(row=3, column=0,sticky=W)

        # флажок 'буква - 3'
        self.number3=BooleanVar()
        Checkbutton(self,text = '4', variable = self.number3, command = self.sum).\
            grid(row=4, column=0,sticky=W)

        # флажок 'Буква - 4 '
        self.number4=BooleanVar()
        Checkbutton(self,text = '8', variable = self.number4, command = self.sum).\
            grid(row=5, column=0, sticky=W)

        # флажок 'Буква - 5 '
        self.number5 = BooleanVar()
        Checkbutton(self,text='16', variable=self.number5, command=self.sum).\
            grid(row=6, column=0, sticky=W)

        # текстовая область с результатом
        self.results_txt = Text(self, fg='black', font='Comfortaa 18', width=25, height=3,
                                wrap=WORD)
        self.results_txt.grid(row=8, column=0, columnspan=3)
        self.results_txt.delete(0.0, END)

    def sum(self):
        rezult = 0
        if self.number1.get(): rezult += 1
        if self.number2.get(): rezult += 2
        if self.number3.get(): rezult += 4
        if self.number4.get(): rezult += 8
        if self.number5.get(): rezult += 16
        '''if not self.number1.get() and not self.number1.get() and not self.number1.get() \
                and not self.number1.get() and not self.number1.get(): self.results_txt.delete(0.0, END)'''
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, str(rezult))

screen = Tk()
screen.title('Использование флажков')
screen.geometry('340x300')
screen.resizable(width=False,height=False)
app4 = Task(screen)
screen.mainloop()
