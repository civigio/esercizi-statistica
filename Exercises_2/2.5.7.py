import numpy as np
import math

def mean(array):
	num = np.sum(array)
	mean_n = num / len(array)
	return mean_n
	
def variance(array, square):
	addend1 = mean(square)
	addend2 = mean(array)*mean(array)
	variance_n = addend1-addend2
	return variance_n
	
def standard_dev(array, square):
	dev = math.sqrt(variance(array, square))
	return dev
	
def standard_err(array, square):
	err = standard_dev(array, square)/(math.sqrt(len(array)))
	return err

	

	
	
list = [1, 2, 3, 4, 5]
array = np.array(list)
square = array * array

print(mean(array))
print(variance(array, square))
print(standard_dev(array, square))
print(standard_err(array, square))
