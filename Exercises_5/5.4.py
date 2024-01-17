import numpy as np
import math
import statistics

def main():

    data = np.loadtxt('eventi_unif (1).txt')

    mean = np.mean(data)

    list1 = list(filter(lambda x: x<mean, data))
    list2 = list(filter(lambda x: x>=mean, data))

    stderr = math.sqrt(np.var(data))
    stderr1 = math.sqrt(np.var(list1))
    stderr2 = math.sqrt(np.var(list2))

    print(stderr, stderr1, stderr2)
    print(math.sqrt(statistics.pvariance(data)))

if __name__ == '__main__':
    main()