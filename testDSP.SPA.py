import os
import numpy as np
from numpy import linalg as LA

import DSP

os.system('clear')

A = np.matrix([[1,5,3,2],[4,2,2,3],[9,8,6,4],[5,3,6,8],[8,6,4,2],[0,9,0,9]],float)
print "A:"
print A
print ""

E , PPI = DSP.SPA(A,3)
print "E:"
print E
print "PPI:"
print PPI
