import random
import matplotlib.pyplot as plt
import numpy as np

def rand_range (xMin, xMax) :
    '''
    generazione di un numero pseudo-casuale distribuito fra xMin ed xMax
    '''
    return xMin + random.random () * (xMax - xMin)

def rand_TAC (f, xMin, xMax, yMax) :
    '''
    generazione di un numero pseudo-casuale 
    con il metodo try and catch
    '''
    x = rand_range (xMin, xMax)
    y = rand_range (0, yMax)
    while (y > f (x)) :
        x = rand_range (xMin, xMax)
        y = rand_range (0, yMax)
    return x

list=[]
def func(x): return x**2

for i in range(1000000):
    list.append(rand_TAC(func, 0, 100, 10000))

print(list)

fig, ax = plt.subplots (nrows = 1, ncols = 1)
ax.hist (list,
         color = 'orange',
         bins=100
        )
plt.show()