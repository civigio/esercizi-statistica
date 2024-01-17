import numpy as np
import scipy.stats as st
from iminuit.cost import ExtendedBinnedNLL
from iminuit.minuit import Minuit
from IPython.display import display
import math
import matplotlib.pyplot as plt


def mod_total(bin_edges, N_signal, mu, sigma, N_background, tau):
    return N_signal * st.norm.cdf(bin_edges, mu, sigma) + N_background * st.expon.cdf(bin_edges, 0, tau)


sample = np.loadtxt('dati.txt')

bin_edges = np.linspace(math.floor(min(sample)), math.ceil(max(sample)), math.ceil(1 + 3.322 * np.log(len(sample))))
bin_content, bin_edges = np.histogram(sample, bin_edges)

my_cost_function = ExtendedBinnedNLL(bin_content, bin_edges, mod_total)
my_minuit = Minuit(my_cost_function, N_signal=sum(sample), mu=np.mean(sample), sigma=np.std(sample),
                   N_background=sum(sample), tau=1.)

#----------------------------------------------------

# setting the signal to zero for a first background-only preliminary fit
my_minuit.values["N_signal"] = 0
# fixing the value of the signal parameters to a constant value
# (i.e. they are not considered in the fit)
my_minuit.fixed["N_signal", "mu", "sigma"] = True

# temporary mask avoiding the signal region
bin_centres = 0.5 * (bin_edges[1:] + bin_edges[:-1])
my_cost_function.mask = (bin_centres < 5) | (15 < bin_centres)
my_minuit.migrad()

#-------------------------------------------------------

my_cost_function.mask = None # remove mask
my_minuit.fixed = False # release all parameters
my_minuit.fixed["N_background", "tau"] = True # fix background parameters
my_minuit.values["N_signal"] = sum(sample) - my_minuit.values["N_background"] # do not start at the limit
my_minuit.migrad()

#--------------------------------------------

my_minuit.fixed = False # release all parameters
my_minuit.migrad()
print(my_minuit.valid)
display(my_minuit)

#-----------------------------------------------------

fig, ax = plt.subplots(nrows=1, ncols=1)
ax.hist(sample, density=True, label='Data', bins=np.linspace(math.floor(min(sample)), math.ceil(max(sample)), math.ceil(1 + 3.322 * np.log(len(sample)))))
x_coord = np.linspace(0, 20, 100000)
y_coord = []
for element in x_coord:
    y_coord.append(((my_minuit.values[0])/(len(sample))) * st.norm.pdf(element, my_minuit.values[1], my_minuit.values[2]) + ((my_minuit.values[3])/(len(sample)) * st.expon.pdf(element, 0, my_minuit.values[4])))
plt.plot(x_coord, y_coord, label='Function')
ax.set_title('Fit', size=14)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.grid(True)
ax.legend()
plt.show()