import statclass
import random
import numpy as np
import matplotlib.pyplot as plt
import math

def integral(x_min, x_max, y_min, y_max, N_generated, function = lambda x: math.sin(x)):
   x_coord = []
   y_coord = []
   n_hit = 0

   for i in range(N_generated):
       x_coord.append(x_min + random.random() * (x_max - x_min))
       y_coord.append(y_min + random.random() * (y_max - x_min))
    
   for i in range(len(x_coord)):
       if y_coord[i] <= function(x_coord[i]): n_hit = n_hit + 1

   integral_value = ((x_max-x_min)*(y_max-y_min))*(n_hit/N_generated)
   integral_uncertainty = math.sqrt(((((x_max-x_min)*(y_max-y_min))*((x_max-x_min)*(y_max-y_min)))/(N_generated))*(n_hit/N_generated)*(1-(n_hit/N_generated)))
   
   return integral_value, integral_uncertainty

def main():
    x = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
    y_1 = []
    y_2 = []
    for value in x:
        y_1.append(integral(0, math.pi, 0, 2, value)[0])
        y_2.append(integral(0, math.pi, 0, 2, value)[1])

    fig, (ax_1, ax_2) = plt.subplots(1, 2)
    ax_1.scatter(x, y_1, c='red')
    ax_1.set_xscale('log')
    ax_2.scatter(x, y_2, c='blue')
    ax_2.set_xscale('log')
    plt.show()


if __name__ == '__main__':
    main()