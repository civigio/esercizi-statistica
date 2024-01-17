#Use the result from the previous exercise to calculate the statistics 
#of a Poisson distribution varying the mean, from 1 to 250 (how should you sample the interval?).

#Plot the obtained behavior of skewness and kurtosis as function of the Poisson mean.

import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt
import library_montecarlo as mc

def rand_poisson (lambda_value) :
    list=[]
    def func(x): return -((np.log(1-x))*(1))
    for j in range(100000):
        i=0
        delta=0
        while (delta <= lambda_value):
            n = func(mc.rand_range_uniform(0,1))
            delta = delta + n
            i=i+1
        list.append(i-1)

    return list

vector=np.geomspace(1, 250, 20)
print(vector)
skewness=[]
kurtosis=[]

for lambdavalue in vector:
    k=rand_poisson(lambdavalue)
    skewness.append(sp.skew(k))
    kurtosis.append(sp.kurtosis(k))


fig, ax = plt.subplots (nrows = 1, ncols = 2)

ax[0].plot (vector, skewness, 'bo--')
ax[0].set_title ('Skewness', size=14)
ax[0].set_xlabel ('Lambda')
ax[0].set_ylabel ('Skewness')
ax[0].legend ()
ax[0].grid()

ax[1].plot (vector, kurtosis, 'bo--')
ax[1].set_title ('Kurtosis', size=14)
ax[1].set_xlabel ('Lambda')
ax[1].set_ylabel ('Kurtosis')
ax[1].legend ()
ax[1].grid()

plt.show()