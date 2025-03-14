import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#создаем данные для сферы
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

#радиус сферы
r = 1

#координаты x,y,z
x = r*np.sin(phi)*np.cos(theta)+10
y = r*np.sin(phi)*np.sin(theta)+10
z = r * np.cos(phi)+10

#создаем фигуру и ось 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#рисуем поверхность сферы
ax.plot_surface(x,y,z, color='black', alpha = 0.6)

#настраиваем отображение
ax.set_title("3D отрисовка сферы")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()