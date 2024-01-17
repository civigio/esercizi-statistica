#Generate a sample of pseudo-random numbers distributed according to an 
#exponential density distribution with a characteristic time t0 of 5 seconds.
#Visualize the distribution of the obtained sample in a histogram using the inverse function method.
#Write all functions responsible for random number generation in a library, 
#implemented in separate files from the main program.

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
def func(x): return -((np.log(1-x))*(5))

for i in range(100000):
    list.append(func(rand_range(0,1)))

print(list)

fig, ax = plt.subplots (nrows = 1, ncols = 1)
ax.hist (list,
         color = 'orange',
         bins=int(np.ceil(1+3.322*np.log(100000)))
        )
plt.show()