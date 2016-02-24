import numpy as np
from numpy import pi
from scipy import integrate
import matplotlib.pyplot as plt

fC = lambda x: np.cos(pi * np.square(x) / 2)
fS = lambda x: np.sin(pi * np.square(x) / 2)
C = lambda u: np.array(integrate.quad(fC, 0, u))    
S = lambda u: np.array(integrate.quad(fS, 0, u))   

# Define constants
wavelength = 0.01 # 1cm
# aperture width
d = 0.1 # 10cm
# distances to screen
D1 = 0.3
D2 = 0.5
D3 = 1.0
# Converting range of integration
def x_to_u(x, D):
    return x * np.sqrt(2/wavelength/D)

# point of interest on the screen, from the central axis.
y = np.linspace(0,1,100)

I_integral = lambda u1, u2: np.sqrt(np.square(C(u1)[0] - C(u2)[0]) + np.square(S(u1)[0] - S(u2)[0]))

def intensity(y, D):
    u1 = x_to_u(y - d/2, D1)
    u2 = x_to_u(y + d/2, D1)
    I = np.zeros(len(u1))
    for ii in range(0, len(u1)):
        I[ii] = I_integral(u1[ii], u2[ii]) 
    
    return I


plt.plot(y, intensity(y, D1))















