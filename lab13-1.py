from tkinter import *
'''def lucas_lehmer_test(p, m):
    s = 4
    for _ in range(p - 2):
        s = ((s * s) - 2) % m
    return s == 0
def prime_test_list(n, known_primes):
    if n < 2:
        return False
    if n % 2 == 0:
         return n == 2 # 2 is the only even prime
    k = 0
    while known_primes[k] ** 2 <= n:
        if n % known_primes[k] == 0:
            return False
        k += 1
        return True
def mersenne_prime_print_list(a):
    known_primes = [2]
    known_mersenne_primes = [3]
    for n in range(3, a, 2):
        if prime_test_list(n, known_primes):
            known_primes.append(n)
            m = 2 ** n - 1
            if lucas_lehmer_test(n, m):
                known_mersenne_primes.append(m)
    return known_mersenne_primes'''
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