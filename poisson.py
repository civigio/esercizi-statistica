import random
import numpy as np

def exp_rand(tau):
	return - tau * np.log(1. - random.random())

def pois_rand(mu):
	'''
	return random poisson distributed numbers.
	it uses the first function and exploits the fact that time intervals between poissonian events are exponential distributed
	'''
	
	# for the sake of simplicity we set an unitary measurement time and consequently the proper characteristic time
	tM = 1.
	t0 = 1. / mu
	
	# array to collect the extremes of the time intervals
	intervals = []

	# the inital time is 0
	t = 0.
	
	# the first interval ends at the time newt
	newt = exp_rand(t0)

	# update the time
	t += newt

	# go on until the measurement time is surpassed
	while(t < tM):
		intervals.append(newt) # saves the extreme of the time interval
		newt = exp_rand(t0) # new interval
		t += newt
	return len(intervals)