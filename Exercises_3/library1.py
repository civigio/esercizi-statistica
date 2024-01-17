import numpy as np
import matplotlib.pyplot as plt

def sturges (N_events):
    return int(np.ceil(1+3.322*np.log(N_events)))

def gc_read(): #legge un file e crea un array
    name_file=input()
    with open(name_file) as input_file:
        sample = [float(x) for x in input_file.readlines()]
        npsample = np.array(sample)
    return npsample

def gc_moments(npsample): #restituisce media, varianza, deviazione standard e errore standard
    mean = np.mean(npsample)
    variance = np.var(npsample)
    stdev = np.std(npsample)
    sterr = stdev/len(npsample)
    return mean, variance, stdev, sterr

def gc_display(npsample): #plotta l'istogramma
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (npsample, bins=sturges(len(npsample)), color = 'orange')
    plt.show()