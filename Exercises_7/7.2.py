#Use the result from the first exercise to simulate a countng experiment with Poisson characteristics:

#Choose a characteristic time t0 for a radioactive decay process;
#Choose a measurement time tM for the counting window;
#In a loop, simulate N pseudo-experiments of counting, where, 
    #for each of them, a sequence of random events is generated with an intertime 
    #characteristic of Poisson phenomena, until the total time elapsed is greater 
    #than the measurement time, counting the number of generated events that fall within the interval.
#Fill a histogram with the simulated counts for each experiment.

import random
import matplotlib.pyplot as plt
import numpy as np

def rand_range (xMin, xMax) :
    return xMin + random.random () * (xMax - xMin)

def func(x): return -((np.log(1-x))*(t_0))

list=[]
t_0=0.5
intervaltime=5

for j in range(100000):
    i=0
    delta=0
    while (delta <= intervaltime):
        n = func(rand_range(0,1))
        delta = delta + n
        i=i+1
    list.append(i-1)

fig, ax = plt.subplots (nrows = 1, ncols = 1)
ax.hist (list,
         color = 'orange',
         bins=len(np.unique(list))
        )
ax.grid()
plt.show()