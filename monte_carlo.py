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
    f_x = [monte_carlo_step(f, upper,lower) for ii in step]

    f_x_squared = [np.power(f_x,2) for fx in f_x]
    f_bar = np.mean(f_x)
    f2_bar = np.mean(f_x_squared)
    
    return [f_bar, f2_bar] 

def monte_carlo_integration(upper, lower, no_of_samples):
    [f_bar, f2_bar] = monte_carlo_integration_unit(upper, lower, no_of_samples)
    
    V = np.power((upper - lower),8)

    integration_result = V * f_bar
    error = V * np.sqrt((f2_bar-f_bar*f_bar)/no_of_samples)

    return [integration_result, error]

t1 = time()
print monte_carlo_integration(np.pi/8, 0, 5000)
t2 = time()
print t2 - t1
        
    
    

    
    
    
    













