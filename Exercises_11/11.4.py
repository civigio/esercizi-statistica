import numpy as np
import matplotlib.pyplot as plt
import random
from iminuit import Minuit
from iminuit.cost import LeastSquares


def func(x, m, q):
    return (m * x) + q


def generate_uniform(n, low, high):
    uniform_values = []
    for i in range(n):
        uniform_values.append(random.random() * (high - low) + low)
    return uniform_values


def generate_set(n, low, high, p1, p2, function, epsilon_fixed):
    epsilon = np.random.normal(loc=0, scale=epsilon_fixed, size=n)
    x_coord = generate_uniform(n, low, high)
    y_coord = []
    for i in range(len(x_coord)):
        y = function(x_coord[i], p1, p2) + epsilon[i]
        y_coord.append(y)
    return x_coord, y_coord


def main():
    q = []

    for i in range(10000):
        fixed_epsilon = 1

        coordinates = generate_set(10, 0, 10, 1, 2, func, fixed_epsilon)

        least_squares = LeastSquares(coordinates[0], coordinates[1], fixed_epsilon, func)
        my_minuit = Minuit(least_squares, m=0, q=0)  # starting values for m and q
        my_minuit.migrad()  # finds minimum of least_squares function
        my_minuit.hesse()  # accurately computes uncertainties

        q.append(my_minuit.fval)

    fig, ax = plt.subplots()
    ax.hist(q)
    plt.show()

    print(np.average(q))
    print(my_minuit.ndof)

    return


if __name__ == '__main__':
    main()
