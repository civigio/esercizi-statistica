import random
import matplotlib.pyplot as plt
import numpy as np

def rand_range(xMin, xMax):
    '''
    Generazione di un numero pseudo-casuale distribuito fra xMin ed xMax
    '''
    return xMin + random.random() * (xMax - xMin)

def func(x, tau):
    return -np.log(1 - x) * tau

def likelihood(lst):
    return np.prod(lst)

tau = 2
log_likelihood_values = []
repetition = np.arange(1, 401, 5)

for i in repetition:
    log_list = []
    for _ in range(i):
        log_list.append(rand_range(0, 1))
    exponential_pdf = func(np.array(log_list), tau)
    exponential = (1 / tau) * np.exp(-exponential_pdf / tau)
    log_likelihood_value = np.log(likelihood(exponential))
    log_likelihood_values.append(log_likelihood_value)

log_likelihood_values = np.array(log_likelihood_values)

fig, ax = plt.subplots(1, 1)
plt.plot(repetition, log_likelihood_values)
plt.xlabel('Repetition')
plt.ylabel('Log Likelihood')
plt.title('Log Likelihood vs Repetition')
plt.grid(True)
plt.show()