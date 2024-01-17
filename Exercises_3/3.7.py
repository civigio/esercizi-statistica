from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt 

mean = 1.
sigma = 0.5

norm_fix = norm (mean, sigma)

x_values=np.linspace(-2, 4, 10000)
y_values=norm_fix.pdf(x_values)
cdf=norm_fix.cdf(x_values)

fig, ax=plt.subplots (nrows=1, ncols=1)
ax.plot(x_values, y_values)
ax.plot(x_values, cdf)
plt.show()