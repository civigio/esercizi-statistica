import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from math import floor
import scipy.stats as sp

def rand_range (xMin, xMax) :
    '''
    generazione di un numero pseudo-casuale distribuito fra xMin ed xMax
    '''
    return xMin + random.random () * (xMax - xMin)

def rand_TCL (xMin, xMax, N_sum = 10) :
    '''
    generazione di un numero pseudo-casuale 
    con il metodo del teorema centrale del limite
    su un intervallo fissato
    '''
    y = 0.
    for i in range (N_sum) :
        y = y + rand_range (xMin, xMax)
    y /= N_sum 
    return y 

def generate_TCL (xMin, xMax, N, N_sum = 10, seed = 0.) :
    '''
    generazione di N numeri pseudo-casuali
    con il metodo del teorema centrale del limite, in un certo intervallo,
    a partire da un determinato seed
    '''
    if seed != 0. : random.seed (float (seed))
    randlist = []
    for i in range (N):
        # Return the next random floating point number in the range 0.0 <= X < 1.0
        randlist.append (rand_TCL (xMin, xMax, N_sum))
    return randlist

def main () :

    xMin  = float (-5)  # minimum of the histogram drawing range
    xMax  = float (5)  # maximum of the histogram drawing range
    seed  = float (random.randint(1, 100))
    N     = int (100000)
    N_sum = int (8)

    print (' -------- ')
    print (' minimum : ', xMin)
    print (' maximum : ', xMax)
    print (' seed    : ', seed)
    print (' N       : ', N)
    print (' N_sum   : ', N_sum)
    print (' -------- ')

    randlist = generate_TCL (xMin, xMax, N, N_sum, seed)

    print(np.mean(randlist))
    print(np.var(randlist))
    print(sp.skew(randlist))
    print(sp.kurtosis(randlist))


    # plotting of the generated list of numbers in a histogram

    nBins = floor (len (randlist) / 400.)             # number of bins of the hitogram
    bin_edges = np.linspace (xMin, xMax, nBins + 1)  # edges o the histogram bins

    # disegno della funzione
    fig, ax = plt.subplots ()
    ax.set_title ('Histogram of random numbers', size=14)
    ax.set_xlabel ('random value')
    ax.set_ylabel ('events in bin')
    ax.hist (randlist,      # list of numbers
             bins = bin_edges,
             color = 'orange',
             # normed = True,
            )

    plt.show ()


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


if __name__ == "__main__":
    main ()