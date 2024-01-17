import math
import matplotlib.pyplot as plt
import numpy as np

def minimum_point(f, xMin, xMax, precision = 0.0001):
    r = ((math.sqrt(5)-1)*0.5)
    
    while ((xMax - xMin)>precision):
        over = xMin + r*(xMax - xMin)
        under = xMax - r*(xMax - xMin)
        if (f(under)>f(over)): xMin = under
        else: xMax = over

    return ((xMax + xMin)*0.5)

def main():
    value = minimum_point((lambda x: x**2 +7.3*x +4), -10, 10)
    print(value)

    fig, ax = plt.subplots(1, 1)
    x_coord=np.linspace(-10, 10, 10000)
    y_coord=(lambda x: x**2 +7.3*x +4)(x_coord)
    x_point=np.full(10000, value)
    y_point=np.linspace(-20, 10, 10000)
    ax.plot(x_coord, y_coord)
    ax.plot(x_point, y_point)
    ax.grid()
    plt.show()
    return

if __name__ == '__main__':
    main()