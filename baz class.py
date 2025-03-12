import matplotlib.patches
import matplotlib.pyplot as plt
import math
import numpy as np


class Baza:
    def __init__(self, side,a,b,c,x):
        self.side = side
        self.a = a
        self.b = b
        self.c = c
        x = x
        self.form = ((a*x)^2+b*x+c ) 

print('Квадратическая функция y=ax^2+bx+c. Введите параметры.') 
a = float(input('a = ')) 
b = float(input('b = ')) 
c = float(input('c = '))  

x = np.linspace(-100, 100, 1000) 
y = a*x**2 + b*x + c     

fig, ax = plt.subplots() 
ax.plot(x, y) 
plt.show()












