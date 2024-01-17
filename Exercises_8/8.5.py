import statclass
import random
import numpy as np
import matplotlib.pyplot as plt

def inverse_cdf(rand):
    return (-2)*np.log(1-rand)

individual_std = []
sample_std = []

N_toy = 10
N_max = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]

for value in N_max:
    means = []
    sigma_means = []
    for i in range(N_toy):
        randlist = []
        for j in range(value):
            randlist.append(inverse_cdf(random.random()))
        toy_stats = statclass.stats(randlist)
        means.append(toy_stats.mean())
        sigma_means.append(toy_stats.sigma_mean())
    toy_means = statclass.stats(means)
    individual_std.append(sigma_means[0])
    sample_std.append(toy_means.sigma_mean())

fig, ax = plt.subplots(1, 1)
ax.scatter(N_max, individual_std, c='blue')
ax.scatter(N_max, sample_std, c='green')
ax.legend()
plt.show()
