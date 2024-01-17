import numpy as np
import time

def median(array):
	sorted = np.sort(array)
	i=len(sorted)//2
	return sorted[i]



list1=[5, 3, 7, 1, 9]
array1=np.array(list1)

time1 = time.time()
median(array1)
time2 = time.time()

print(median(array1))
print(time2-time1)
