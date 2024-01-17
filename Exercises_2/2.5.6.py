import numpy as np

def limit(array, i):
	sorted = np.sort(array)
	line = int(len(sorted)//(1/i))
	print(sorted[line])
	print(sorted[len(sorted)-line-1])
	return
	
	
	
	
list_casual = [1, 3, 5, 7, 9]
i = float(input())
array = np.array(list_casual)
limit(array, i)

