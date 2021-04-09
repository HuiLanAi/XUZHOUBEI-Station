from matplotlib import pyplot as plt
import numpy as np
import math
import scipy.stats as stats

# x = np.linspace(-2*np.pi, 2*np.pi, 1000)
# y = np.sin(x)
# z = np.sin(x+0.5*np.pi)
# k = np.sin(0*x)
# p = np.sin(x*0.6)
# plt.plot(x, y)
# plt.plot(x, z)
# plt.plot(x, p, ls='--')
# plt.plot(x, k, color='black')


print(stats.norm(0.5, 0.40824829).cdf(0.5))
