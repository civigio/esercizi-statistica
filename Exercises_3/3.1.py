import numpy as np
import matplotlib.pyplot as plt

sample = np.array([3, 2, 3, 4, 3])

fig, ax=plt.subplots (nrows=1, ncols=1)
ax.hist(sample, bins=3)
plt.show()
plt.savefig('3.7.1.png')