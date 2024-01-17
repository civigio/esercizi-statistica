from scipy.integrate import quad
from scipy.stats import norm

mean = 1.
sigma = 0.5

norm_fix = norm (mean, sigma)

area1 = 1-(2*quad(norm_fix, 1, sigma))
area2 = 1-(2*quad(norm_fix, 1, 2*sigma))
area3 = 1-(2*quad(norm_fix, 1, 3*sigma))
area4 = 1-(2*quad(norm_fix, 1, 4*sigma))
area5 = 1-(2*quad(norm_fix, 1, 5*sigma))

print(area1, area2, area3, area4, area5)