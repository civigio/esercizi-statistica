import random
import numpy as np
import matplotlib.pyplot as plt


def rand_range_uniform (xMin, xMax) :
    '''
    generazione di un numero pseudo-casuale distribuito fra xMin ed xMax
    '''
    return xMin + random.random () * (xMax - xMin)

def rand_exponential (t_0) :
    '''
    generazione di un array di numeri pseudo-casuali distribuiti secondo
    una pdf esponenziale con tempo caratteristico t_0
    '''
    list=[]
    def func(x): return -((np.log(1-x))*(t_0))
    for i in range(100000):
        list.append(func(rand_range_uniform(0,1)))

    return list

def rand_poisson (lambda_value) :
    '''
    generazione di un array di numeri pseudo-casuali distribuiti secondo
    una pdf poissoniana con valore medio lambda
    '''
    list=[]
    def func(x): return -((np.log(1-x))*(1))
    for j in range(100000):
        i=0
        delta=0
        while (delta <= lambda_value):
            n = func(rand_range_uniform(0,1))
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

    return list