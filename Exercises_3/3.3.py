import sys
import numpy as np
import matplotlib.pyplot as plt

with open('eventi_gauss.txt') as input_file:
    sample = [float(x) for x in input_file.readlines()]

reduced=np.ones(int(sys.argv[1]))
for i in range(int(sys.argv[1])):
    reduced[i]=sample[i]

fig, ax = plt.subplots (nrows = 1, ncols = 1)
ax.hist (reduced, color = 'orange')
plt.show()