import numpy as np
from time import time

def f(x):
    sum_of_x = sum(x_value for x_value in x)
    value = np.sin(sum_of_x) * np.power(10,6)
    return value
    return 1
    
def monte_carlo_step(f, upper, lower, no_of_variables=8):
    x = lower + (upper - lower) * np.random.random(no_of_variables)
    #x = [1,1,1,1,1,1,1,1]
    return f(x)

def monte_carlo_integration_unit(upper, lower, no_of_samples):
    step = range(0,no_of_samples)
    f_x = 0
    f_x2 = 0
    
    for ii in step:
        f_x_unit = monte_carlo_step(f, upper,lower)
        f_x = f_x + f_x_unit
        f_x2 = f_x2 + np.power(f_x_unit,2)

    return [f_x, f_x2] 

def monte_carlo_integration(upper, lower, no_of_samples):
    M = monte_carlo_integration_unit(upper, lower, no_of_samples)
    [f_bar, f2_bar] = np.divide(M,no_of_samples)
    
    V = np.power((upper - lower),8)
    
    print f2_bar
    
    integration_result = V * f_bar
    error = V * np.sqrt((f2_bar-f_bar*f_bar)/no_of_samples)

    return [integration_result, error]

t1 = time()
print monte_carlo_integration(np.pi/8, 0, 10000)
t2 = time()
print t2 - t1
        
    
    

    
    
    
    













