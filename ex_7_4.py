'''
Use the result from the previous exercise to calculate the statistics of a Poisson distribution varying the mean, from 1 to 250 (how should you sample the interval?).
Plot the obtained behavior of skewness and kurtosis as function of the Poisson mean.
'''

import sys
import poisson as ps
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats
import time

def main():
	N = 1000000		# number of counting experiments
	n_means = 25	# number of means to study

	stddevs = []	# array to store the standard deviations
	skews = []		# array to store the skewenesses
	kurts = []		# array to store the kurtosis

	mus = np.logspace(0, np.log(250), n_means, endpoint=True, base=np.exp(1)) # list of log distruted means to study
	x = np.linspace(1, 250, 24000)
	# print(mus) # debug

	time_start = time.time()

	for mu in mus:
		counts = []									# array to store the countings
		for k in range(N):
			counts.append(ps.pois_rand(mu))			# single counting experiment
		stddevs.append(np.std(counts))
		skews.append(scipy.stats.skew(counts))
		kurts.append(scipy.stats.kurtosis(counts))
	
	time_end = time.time()

	# print("time elapsed: ", time_end - time_start) # debug
	
	fig, axes = plt.subplots(nrows = 1, ncols = 3)
	fig.suptitle("standard deviations, skewenesses, kurtosis observed in $N={}$ counting experiments with variable means compared with the expected ones. (time elapsed: ~{} min)".format(N, round((time_end - time_start)/60)))
	axes[0].set_xlabel("means")
	axes[0].set_ylabel("standard deviations")
	axes[0].scatter(mus, stddevs, s=5, color='navy')
	axes[0].plot(x, (lambda x : np.sqrt(x))(x), color='coral')
	axes[1].set_xlabel("means")
	axes[0].set_ylabel("skewnesses")
	axes[1].scatter(mus, skews, s=5, color='navy')
	axes[1].plot(x, (lambda x : 1. / np.sqrt(x))(x), color='coral')
	axes[2].set_xlabel("means")
	axes[0].set_ylabel("kurtosis")
	axes[2].scatter(mus, kurts, s=5, color='navy')
	axes[2].plot(x, (lambda x : 1. / x)(x), color='coral')
	plt.show()
		
		
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

if __name__ == "__main__":
    main()
