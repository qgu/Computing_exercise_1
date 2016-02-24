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
    
    integration_result = V * f_bar
    error = V * np.sqrt((f2_bar-f_bar*f_bar)/no_of_samples)

    return [integration_result, error]

def estimated_computation_time(no_of_samples):
    return 0.0000331 * no_of_samples

range_of_samples = [10**x for x in range(2,5)]
no_of_repeats = 10
x = np.arange(0,100)
results = np.zeros(no_of_repeats)

with open('test_file','w+') as file:
    for no_of_samples in range_of_samples:
        for ii in range(0,no_of_repeats):
            M = monte_carlo_integration(np.pi/8, 0, no_of_samples)
            results[ii] = M[0]
        file.write( str(no_of_samples) + str(np.std(results))[1:-2] )
    

    
    

    
    
    
    













