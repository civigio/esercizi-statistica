import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x_coord = np.linspace(0, 2*np.pi, 10_000)
y_coord_1 = np.sin(x_coord)
y_coord_2 = np.cos(x_coord)
y_coord_3 = np.sin(x_coord - 1)+4
y_coord_4 = np.sin(x_coord - 1)
y_coord_5 = np.cos(x_coord * 2)
y_coord_6 = np.cos(x_coord *2)*3
ax.plot(x_coord, y_coord_1, label='sin(x)')
ax.plot(x_coord, y_coord_2, label='cos(x)')
ax.plot(x_coord, y_coord_4, label='sin(x-1)')
ax.plot(x_coord, y_coord_3, label='sin(x-1)+4')
ax.plot(x_coord, y_coord_5, label='sin(2x)')
ax.plot(x_coord, y_coord_6, label='3sin(2x)')
ax.legend()
plt.grid(True)
plt.show()


