import numpy as np
import matplotlib.pyplot as plt

with open('eventi_gauss.txt') as input_file:
    sample1 = [float(x) for x in input_file.readlines()]

with open('eventi_unif.txt') as input_file:
    sample2 = [float(x) for x in input_file.readlines()]

fig, ax = plt.subplots (nrows = 1, ncols = 1)
ax.hist (sample1, color = 'orange', alpha=0.5)
ax.hist (sample2, color = 'blue', alpha=0.5)
plt.show()