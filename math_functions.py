import math
import numpy as np
from numpy.core.fromnumeric import var


# building my own sigma function for practice
def sigma(n):
    '''compute the standard deviation'''
    x = abs(n - np.mean(n))**2
    print(f"x is\n{x}")
    # print(f"deviations are:\n{math.sqrt(x)}")
    sd = math.sqrt(np.mean(x))
    return sd

my_data = [1, 12, 16, 3, 14, 5, 6]
mu = np.mean(my_data)
sd = np.std(my_data)
my_sd = sigma(my_data)

print(f"built in average: {mu}")
print(f"built in sd: {sd}")
print(f"my sd function: {my_sd}")