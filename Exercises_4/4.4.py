import random
import matplotlib.pyplot as plt
import numpy as np

randlist=[]
for i in range (100000):
    randlist.append (random.randint (0, 100))
    print (i, randlist[-1])

bin_edges = np.linspace (0, 100, 102)

fig, ax = plt.subplots (nrows = 1, ncols = 1)
ax.hist (randlist,
         color = 'orange',
         bins=bin_edges
        )
plt.show()