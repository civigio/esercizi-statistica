import scipy.stats as sp
import numpy as np
import math

with open('eventi_unif.txt') as input_file:
    sample1 = [float(x) for x in input_file.readlines()]

print(np.mean(sample1))
print(np.var(sample1))
print(np.std(sample1))
stderr=np.std(sample1)/math.sqrt(len(sample1))
print(stderr)