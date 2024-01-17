from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt 

expon_fix = expon()

x_values=np.linspace(0, 10, 10000)
y_values=expon_fix.pdf(x_values)
cdf=expon_fix.cdf(x_values)

fig, ax=plt.subplots (nrows=1, ncols=1)
ax.plot(x_values, y_values)
ax.plot(x_values, cdf)
plt.show()