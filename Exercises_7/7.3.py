#Use the source code written in the previous exercise to add to the library 
#developed for exercise 1 a function that generates random numbers according 
#to the Poisson distribution, with the mean expected events as an input parameter.

#Rewrite the previous exercise using this function, also drawing the probability density histogram.

#Calculate the sample statistics (mean, variance, skewness, kurtosis) 
#from the input list using a library.

#Use the generated sample to test the functionality of the library.

import library_montecarlo as mc
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp

'''poisson=mc.rand_poisson(10)'''
def rand_poisson (lambda_value) :
    '''
    generazione di un array di numeri pseudo-casuali distribuiti secondo
    una pdf poissoniana con valore medio lambda
    '''
    list=[]
    def func(x): return -((np.log(1-x))*(1))
    for j in range(1000):
        i=0
        delta=0
        while (delta <= lambda_value):
            n = func(mc.rand_range_uniform(0,1))
            delta = delta + n
            i=i+1
        list.append(i-1)

    return list

for i in range(20):
    poisson=rand_poisson(10)
    print(np.mean(poisson))
    print(np.var(poisson))
    print(sp.skew(poisson))
    print(sp.kurtosis(poisson))
    print('----------')
