

import math
import numpy as np


a, E  = np.loadtxt('data', usecols=(0,1), delimiter='\t', unpack = True)	
x  = (a*3.5999)**(-2)

p = np.polyfit(x, E, 3)

c0 = p[3]
c1 = p[2]
c2 = p[1]
c3 = p[0]

#print 'The fitted BM equation is:'
#print ' y = %.4f * (x**3) + %.4f * (x**2) + %.4f * (x) + %.4f' %(c3,c2,c1,c0)

# Get the results of c_1 + 2c_2x + 3c_3x^2 = 0 
x1 = (math.sqrt(4*c2**2 - 12*c1*c3) - 2*c2)/(6*c3) 
para = 1/math.sqrt(x1)

print  (para) 

