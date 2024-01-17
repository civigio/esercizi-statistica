import numpy as np
import matplotlib.pyplot as plt

def sturges (N_events):
    return int(np.ceil(1+3.322*np.log(N_events)))

def main():

    data=np.loadtxt('eventi_gauss (1).txt')
    N=len(data)

    square = list(map(lambda x: x*x, data))
    cube = list(map(lambda x: x*x*x, data))

    fig, ax = plt.subplots(1,1)
    ax.hist(data, color='red', alpha=0.6, bins=sturges(N))
    ax.hist(square, color='blue', alpha=0.4, bins=sturges(N))
    ax.hist(cube, color='green', alpha=0.4, bins=sturges(N))

    plt.show()

if __name__ == '__main__':
    main()