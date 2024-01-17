import random
import matplotlib.pyplot as plt
import numpy as np
import math

def rand_range (xMin, xMax) :
    '''
    generazione di un numero pseudo-casuale distribuito fra xMin ed xMax
    '''
    return xMin + random.random () * (xMax - xMin)

list=[]
def func(x): return -((np.log(1-x))/2)

for i in range(100000):
    list.append(func(rand_range(0,1)))

print(list)

fig, ax = plt.subplots (nrows = 1, ncols = 1)
ax.hist (list,
         color = 'orange',
         bins=100
        )
plt.show()