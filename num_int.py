import numpy as np
from numpy import pi
from scipy import integrate

fC = lambda x: np.cos(pi * np.square(x) / 2)
fS = lambda x: np.sin(pi * np.square(x) / 2)
C = lambda u: integrate.quad(fC, 0, u)    
S = lambda u: integrate.quad(fS, 0, u)   

















