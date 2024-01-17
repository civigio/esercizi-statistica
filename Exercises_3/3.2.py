import numpy as np

with open('eventi_unif.txt') as input_file:
    sample = [float(x) for x in input_file.readlines()]

i=0
j=0
while i<10:
    if sample[j]>0:
        print(sample[j])
        i=i+1
    j=j+1

N_events=len(sample)
print("-------", N_events)
ordine=np.sort(sample)
print("-------", ordine[0])
print("-------", ordine[len(ordine)-1])