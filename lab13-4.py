from tkinter import *

class Task(Frame):
    ''' Использование флажков '''
    def __init__(self, master):
        super(Task, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        ''' Создает переключатель '''

        # метка-инструкция
        Label(self,text = 'Контейнеры:', font = 'Comfortaa 18', fg = 'blue').\
            grid(row=0, column=0, sticky=W)
        self.favorite = StringVar()
        self.favorite.set(None)

        # положение переключателя 'String'
        Radiobutton(self,
        text = 'Строки (Strings)', font='15', variable = self.favorite, value = 'Hi', command =
                    self.example).\
            grid(row=1, column=0, sticky=W)

        # положение переключателя 'Lists'
        Radiobutton(self, text = 'Списки (Lists)',font='15', variable = self.favorite, value = [
            'one', 'two','three'],
        command = self.example).grid(row=2, column=0, sticky=W)

        # положение переключателя 'Lists'
        Radiobutton(self,
        text = 'Кортежи (Tuples)',font='15', variable = self.favorite, value = (1, 2, 3), command =
                    self.example).\
            grid(row=3, column=0, sticky=W)
        Radiobutton(self,
                    text='Словари (Dictionaries)',font='15', variable=self.favorite,
                    value={"sun": "a star",
                           "earth": "a planet",
                           "moon": "a satellite"},
                    command = self.example).\
            grid(row=4, column=0, sticky=W)

        # текстовая область для результата
        self.results_txt=Text(self, fg='blue', font='Comfortaa 14', width=60,height = 4,
                              wrap = WORD)
        self.results_txt.grid(row=5, column=0, columnspan=4)


    def example(self):
        message = "Пример данного типа контейнера:\n"
        message += self.favorite.get()
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

screen = Tk()
screen.title('Использование переключателя')
screen.geometry('620x280')
app4 = Task(screen)
screen.mainloop()
