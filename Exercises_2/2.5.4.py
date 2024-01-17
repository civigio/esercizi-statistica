import numpy as np
import time

list_a=[1, 3, 5, 7, 8, 9, 4, 123, 1245, 2687, 3456786, 3456, 12345, 8765]
list_b=[2, 98765, 3456789, 7654, 76543, 2456, 9704, 212453, 92047, 45, 22, 76, 948737, 65]

array_a=np.array(list_a)
array_b=np.array(list_b)



time_snapshot1 = time.time()
print(time_snapshot1)

list_sum=[list_a[i]+list_b[i] for i in range(len(list_a))]

time_snapshot2 = time.time()
print(time_snapshot2)

array_sum = array_a + array_b

time_snapshot3 = time.time()
print(time_snapshot3)

op1 = time_snapshot2-time_snapshot1
op2 = time_snapshot3-time_snapshot2

print(op1)
print(op2)
