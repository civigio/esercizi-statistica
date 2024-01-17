import math
import matplotlib.pyplot as plt
import numpy as np

def bisection(f, xMin, xMax, precision = 0.0001):

    while ((xMax - xMin) > precision):
        xAve = ((xMin + xMax)*0.5)
        if ((f(xMin) * f(xAve)) >0): xMin = xAve
        else: xMax = xAve

    return xAve

def main():
    value = bisection((lambda x: np.cos(x)), 0, 4)
    print(value)

    fig, ax = plt.subplots(1, 1)
    x_coord=np.linspace(0, 4, 10000)
    y_coord=np.cos(x_coord)
    x_point=np.full(10000, value)
    y_point=np.linspace(-1, 1, 10000)
    ax.plot(x_coord, y_coord)
    ax.plot(x_point, y_point)
    ax.grid()
    plt.show()

    return


if __name__ == '__main__':
    main()