import math
import matplotlib.pyplot as plt
import numpy as np


class Uravnenie:


    def __init__ (self,a,b,c):
        self.a = a
        self.b = b 
        self.c = c


    def discriminant(self):
        discr = self.b ** 2 - 4 * self.a * self.c
        print("Дискриминант D = %.2f" % discr)

        if discr > 0:
            x1 = (-self.b + math.sqrt(discr)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discr)) / (2 * self.a)
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif discr == 0:
            x = -self.b / (2 * self.a)
            print("x = %.2f" % x)
        else:
            print("Корней нет")  
    

    def paint(self):
        self.x = np.linspace(-10, 10, 50)
        self.y = self.a*self.x**2 + self.b*self.x + self.c  

        fig, self.ax = plt.subplots()

        self.ax.plot(self.x, self.y, color='black') 
        self.ax.set_title('График функции y') 
        self.ax.set_xlabel('Ось x') 
        self.ax.set_ylabel('Ось y') 
        self.ax.grid() 

        self.ax.set_xlim(-10, 10) 
        self.ax.set_ylim(-10, 10) 


    def show(self):   
        self.paint()
        plt.show() 


class Proizvodnay(Uravnenie):


    def __init__(self,a ,b, c):
        super().__init__(a, b, c)


    def paint(self):
        super().paint()
        self.x = np.linspace(-10, 10, 2)
        self.y = self.a*self.x + self.b
        self.ax.plot(self.x, self.y, color='pink')


print("Введите коэффициенты для уравнения: ")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))


x = Uravnenie(a, b, c)
x = Proizvodnay(a, b, c)
x.discriminant()
x.show()