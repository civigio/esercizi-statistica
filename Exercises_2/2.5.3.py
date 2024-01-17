import numpy as np

even = np.zeros(50)
even[0]=2
for i in range(1, 50):
	even[i]=even[i-1]+2
	
print(even)


odd = np.zeros(50)
odd[0]=1
for i in range(1, 50):
	odd[i]=odd[i-1]+2
	
print(odd)

array=np.add(even, odd)
print(array)
